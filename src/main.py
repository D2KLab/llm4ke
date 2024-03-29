#  Copyright 2024. EURECOM
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# === Import ==================================================================

import logging
import os
import re
import time
from argparse import ArgumentParser
from os import path
from pathlib import Path

import yaml
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_community.llms import Ollama
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from rdflib import Graph, RDF, RDFS, OWL
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

from LocalTemplate import LocalTemplate
from utils import flatten

# === Init ====================================================================

os.environ["CUDA_VISIBLE_DEVICES"] = "3,2"  # Specify the GPU id
os.environ["HUGGINGFACE_HUB_CACHE"] = "/data/huggingface/"

available_llms = {
    "dpo": "yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B",
    "una": "fblgit/UNA-TheBeagle-7b-v1",
    "solar": "bhavinjawade/SOLAR-10B-OrcaDPO-Jawade",
    "zephyr": "HuggingFaceH4/zephyr-7b-beta",
    "llama2": "local",
    "mistral": "local",
    'GPT': "OpenAI"
}

API_KEY = os.getenv("OPENAI_API_KEY")

# device = "cuda"

# ----------------------------------------------------------------------------

logBaseName = "eurecom.llm4ke.prompt"
logFileName = logBaseName + ".log"

loggingFormatString = (
    "%(asctime)s:%(levelname)s:%(threadName)s:%(funcName)s:%(message)s"
)


# === Functions ===============================================================

def simplify(uri):
    """
    Remove useless parts of the URI, such as the namespace, for easier processing.
    :param uri: an URI as a string
    :return: a simpler URI as a string
    """
    return re.split(r'[#/]', uri)[-1].replace('_', ' ')


def select_in_batches(lst, batch_size=20):
    for i in range(0, len(lst), batch_size):
        yield lst[i:i + batch_size]


class CustomHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        formatted_prompts = "\n".join(prompts)
        print(f"********** Prompt **************\n{formatted_prompts}\n********** End Prompt **************")


def select_props_by_class(schema, cl):
    return [p for s, p, o in schema if cl in [s, o]]


def select_schema_by_class(schema, cl):
    return [(s, p, o) for s, p, o in schema if cl in [s, o]]


def run(task, input_path, llm_model, ont_name,
        n_cqs=10, include_description=False, verbose=False, output_path='/out',
        id=None, local_llm=False, n_examples=0
        ):
    """Processing entry point: load the ontology, the prompting template, then call the LLM and save the results.

    :param task:
    :param input_path:
    :param llm_model:
    :param ont_name:
    :param n_cqs:
    :param include_description:
    :param verbose:
    :param output_path:
    :param id:
    :param local_llm:
    :param n_examples:
    :return:
    """

    # Loading the ontology
    g = Graph()

    for g_path in os.listdir(path.join(input_path, 'dm')):
        if not g_path.split('.')[-1] in ['rdf', 'ttl', 'owl']:
            continue
        dm_path = path.join(input_path, 'dm', g_path)
        logging.debug("LOAD:ONTOLOGY:PARSING:dm_path=%s", dm_path)
        g.parse(dm_path)

    # Retrieving classes and properties as lists
    cls = [s for s, p, o in g.triples((None, RDF.type, OWL.Class))]
    props = ([s for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty))] +
             [s for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty))])

    description = Path(path.join(input_path, 'description.txt')).read_text() if include_description else ''

    logging.info("LOAD:ONTOLOGY:STATS:The %s ontology has %s classes and %s properties.", ont_name, len(cls),
                 len(props))
    # print(f'The {ont_name} ontology has {len(cls)} classes and {len(props)} properties')

    schema = []
    for p in props:
        domain = g.value(p, RDFS.domain, None)
        range = g.value(p, RDFS.range, None)

        if domain is not None:
            if range is not None:
                schema.append((simplify(domain), simplify(p), simplify(range)))
            else:
                schema.append((simplify(domain), simplify(p), 'literal'))

    template_path = f'./src/prompt_templates/{task}.yml'
    PROMPT_TEMPLATE = LocalTemplate.load(template_path)
    logging.debug("LOAD:PROMPT_TEMPLATE:template_path=%s:template=%s", template_path, PROMPT_TEMPLATE)

    # Retrieve the essential information from the schema
    classes_batches = [[simplify(elm) for elm in class_set] for class_set in select_in_batches(cls)]
    property_batches = [flatten([select_props_by_class(schema, cl) for cl in batch]) for batch in classes_batches]
    schema_batches = [flatten([select_schema_by_class(schema, cl) for cl in batch]) for batch in classes_batches]

    # Get Competency Question examples from the dataset
    examples = ''
    if n_examples > 0:
        with open(path.join(input_path, 'cqs', 'cqs.yml')) as f:
            ground_truth = yaml.safe_load(f)
        cqs = [c['question'] for c in ground_truth['ontology']['cqs']]

        examples = 'For example:' + '\n -'.join(cqs[:n_examples])
    logging.debug("LOAD:CQS:n_examples=%s:examples=%s", n_examples, examples)

    # Generate prompts
    input_batches = []
    for c_batch, p_batch, s_batch in zip(classes_batches, property_batches, schema_batches):
        ont_input = {
            'name': ont_name,
            'description': description,
            'n': n_cqs,
            'classes': '\n- '.join([simplify(s) for s in c_batch]),
            'properties': '\n- '.join([simplify(s) for s in p_batch]),
            'schema': '\n- '.join([f'({simplify(s)}, {simplify(p)}, {simplify(o)})' for s, p, o in s_batch]),
            'examples': examples
        }
        input_dict = {}
        for x in PROMPT_TEMPLATE.input:
            input_dict[x] = ont_input[x]
        input_batches.append(input_dict)
    logging.debug("PROMPT:PREPARE:input_batches=%s", input_batches)

    # Instanciate LLM
    if local_llm or available_llms[llm_model] == 'local':
        llm = Ollama(model=llm_model)
    elif available_llms[llm_model] == "OpenAI":
        llm = ChatOpenAI(model="gpt-3.5-turbo-0125", openai_api_key=API_KEY)
    else:
        tokenizer = AutoTokenizer.from_pretrained(available_llms[llm_model])

        model = AutoModelForCausalLM.from_pretrained(
            available_llms[llm_model],
            device_map='sequential',
            load_in_8bit=True,
            use_safetensors=True
        )

        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=512
        )

        llm = HuggingFacePipeline(pipeline=pipe)

    output_parser = StrOutputParser()
    prompt = PromptTemplate(
        input_variables=["prompt"] + PROMPT_TEMPLATE.input, template=PROMPT_TEMPLATE.get()
    )
    chain = prompt | llm | output_parser

    # Call LLM
    logging.info("PROMPT:CALL_LLM:%s:engine=%s", 'START', llm)
    config = {"callbacks": [CustomHandler()]} if verbose else {}
    res = chain.batch(input_batches, config=config)
    logging.info("PROMPT:CALL_LLM:%s:res=%s", 'DONE', res)

    # Parse output to extract Competency Questions
    patterns = [r'(\d+)\. (.+)[?.]', r'\s*-\s*(.*?)[?.]', r'CQ\d+: (.+?)\n']
    cqs = []

    for batch in res:
        for pattern in patterns:
            matches = re.findall(pattern, batch)
            if matches:
                for match in matches:
                    if pattern == patterns[0]:
                        cqs.append(match[1])
                    else:
                        cqs.append(match)
    logging.debug("PROMPT:PROCESS_LLM_RESPONSE:len(cqs)=%s", len(cqs))

    # Prepare the file system for saving the results
    output_folder = path.join(output_path, ont_name)
    os.makedirs(output_folder, exist_ok=True)
    logging.info("SAVE:RESULTS:output_folder=%s", output_folder)

    # Saving the results to a file
    id = id if id is not None else time.time()
    output_file = path.join(output_path, ont_name, f'{ont_name}_{id}.txt')
    with open(output_file, 'w') as f:
        f.write('\n'.join(cqs))
    logging.info("SAVE:RESULTS:output_file=%s", output_file)

    # End of run
    # print(res)
    return True, res


# === Main ====================================================================

if __name__ == '__main__':
    # Get tasks from prompt templates
    available_tasks = [x.replace('.yml', '') for x in os.listdir('./src/prompt_templates/')]

    # Define argument parser
    parser = ArgumentParser(
        prog='LLM4ke',
        description='Experiment about LLMs on Knowledge Graphs'
    )
    parser.add_argument(
        'task',
        choices=available_tasks
    )

    parser.add_argument(
        '-i',
        '--input',
        help='Input folder',
        required=True
        # default='./data/Odeuropa/'
    )

    parser.add_argument(
        '-o',
        '--output',
        help='Output folder',
        default='./out/'
    )
    parser.add_argument(
        '--local_llm',
        action='store_true',
        help='If True, use Ollama instead of Hugging Face'
    )

    parser.add_argument(
        '--llm',
        help='LLM to use',
        default='llama2',
        choices=available_llms
    )

    parser.add_argument(
        '--name',
        help='Name of the ontology',
        required=True
    )

    parser.add_argument(
        '-n',
        '--n_cqs',
        help='Number of competency questions to get in output',
        type=int,
        default=10
    )

    parser.add_argument(
        '-x',
        '--n_examples',
        help='Number of example competency questions to provide in input',
        type=int,
        default=0
    )

    parser.add_argument(
        '--include_description',
        help='Include the content of description.txt in the prompt',
        default=False,
        action='store_true'
    )

    parser.add_argument(
        '--verbose',
        help='Print the full prompt',
        default=False,
        action='store_true'
    )

    parser.add_argument(
        '--id',
        help='Id for naming the output file. If absent, it will be a timestamp'
    )

    parser.add_argument(
        "--log",
        type=int,
        choices=[10, 20, 30, 40, 50],
        action="store",
        default=20,
        help="Verbosity (default: INFO) : DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40, CRITICAL = 50",
    )

    # Instanciate argument parser
    args = parser.parse_args()
    _llm = args.llm
    if not args.local_llm:
        selected = _llm
        if selected != "local":
            _llm = selected

    # Configure logger
    logging.basicConfig(format=loggingFormatString, level=args.log)

    # Call the processing function
    logging.info("INIT")
    run_response = run(
        args.task,
        args.input,
        _llm,
        args.name,
        args.n_cqs,
        args.include_description,
        args.verbose,
        args.output,
        args.id,
        args.local_llm,
        args.n_examples
    )

    logging.info("DONE")
