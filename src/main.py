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
from rdflib import Graph, RDF, RDFS, OWL
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

from LocalTemplate import LocalTemplate

os.environ["CUDA_VISIBLE_DEVICES"] = "3,2"  # Specify the GPU id
os.environ["HUGGINGFACE_HUB_CACHE"] = "/data/huggingface/"


# device = "cuda"


def simplify(uri):
    return re.split(r'[#/]', uri)[-1].replace('_', ' ')


def flatten(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list


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


def run(task, input_path, llm_model, ont_name, n_cqs=10, include_description=False, verbose=False, output_path='/out',
        id=None, local_llm=False, n_examples=0):
    g = Graph()
    for g_path in os.listdir(path.join(input_path, 'dm')):
        if not g_path.split('.')[-1] in ['rdf', 'ttl', 'owl']:
            continue
        g.parse(path.join(input_path, 'dm', g_path))

    cls = [s for s, p, o in g.triples((None, RDF.type, OWL.Class))]
    props = ([s for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty))] +
             [s for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty))])

    description = Path(path.join(input_path, 'description.txt')).read_text() if include_description else ''

    print(f'The {ont_name} ontology has {len(cls)} classes and {len(props)} properties')
    schema = []
    for p in props:
        domain = g.value(p, RDFS.domain, None)
        range = g.value(p, RDFS.range, None)

        if domain is not None:
            if range is not None:
                schema.append((simplify(domain), simplify(p), simplify(range)))
            else:
                schema.append((simplify(domain), simplify(p), 'literal'))

    PROMPT_TEMPLATE = LocalTemplate.load(f'./src/prompt_templates/{task}.yml')

    classes_batches = [[simplify(elm) for elm in class_set] for class_set in select_in_batches(cls)]
    property_batches = [flatten([select_props_by_class(schema, cl) for cl in batch]) for batch in classes_batches]
    schema_batches = [flatten([select_schema_by_class(schema, cl) for cl in batch]) for batch in classes_batches]

    examples = ''
    if n_examples > 0:
        with open(path.join(input_path, 'cqs', 'cqs.yml')) as f:
            ground_truth = yaml.safe_load(f)
        cqs = [c['question'] for c in ground_truth['ontology']['cqs']]
        examples = 'For example:' + '\n -'.join(cqs[n_examples])

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

    if local_llm or available_llms[llm_model] == 'local':
        llm = Ollama(model=llm_model)
    else:
        tokenizer = AutoTokenizer.from_pretrained(llm_model)
        model = AutoModelForCausalLM.from_pretrained(llm_model, device_map='sequential',
                                                     load_in_8bit=False, use_safetensors=True)

        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

        llm = HuggingFacePipeline(pipeline=pipe)

    output_parser = StrOutputParser()
    prompt = PromptTemplate(
        input_variables=["prompt"] + PROMPT_TEMPLATE.input, template=PROMPT_TEMPLATE.get()
    )
    chain = prompt | llm | output_parser

    config = {"callbacks": [CustomHandler()]} if verbose else {}
    res = chain.batch(input_batches, config=config)

    # parse output
    patterns = [r'(\d+)\. (.+)[?.]', r'\s*-\s*(.*?)[?.]']
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

    os.makedirs(path.join(output_path, ont_name), exist_ok=True)
    id = id if id is not None else time.time()
    with open(path.join(output_path, ont_name, f'{ont_name}_{id}.txt'), 'w') as f:
        f.write('\n'.join(cqs))
    print(res)


if __name__ == '__main__':
    available_tasks = [x.replace('.yml', '') for x in os.listdir('./src/prompt_templates/')]
    available_llms = {
        "dpo": "yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B",
        "una": "fblgit/UNA-TheBeagle-7b-v1",
        "solar": "bhavinjawade/SOLAR-10B-OrcaDPO-Jawade",
        "zephyr": "HuggingFaceH4/zephyr-7b-beta",
        "llama2": "local",
        "mistral": "local"
    }

    parser = ArgumentParser(
        prog='LLM4ke',
        description='Experiment about LLMs on Knowledge Graphs')
    parser.add_argument('task', choices=available_tasks)
    parser.add_argument('-i', '--input', help='Input folder', default='./data/Odeuropa/')
    parser.add_argument('-o', '--output', help='Output folder', default='./out/')
    parser.add_argument('--local_llm', action='store_true', help='If True, use Ollama instead of Hugging Face')
    parser.add_argument('--llm', help='LLM to use', default='llama2', choices=available_llms)
    parser.add_argument('--name', help='Name of the ontology', required=True)
    parser.add_argument('-n', '--n_cqs', help='Number of competency questions to get in output', default=10)
    parser.add_argument('-x', '--n_examples', help='Number of example competency questions to provide in input',
                        default=0)
    parser.add_argument('--include_description', help='Include the content of description.txt in the prompt',
                        default=False, action='store_true')
    parser.add_argument('--verbose', help='Print the full prompt',
                        default=False, action='store_true')
    parser.add_argument('--id', help='Id for naming the output file. If absent, it will be a timestamp')

    args = parser.parse_args()
    _llm = args.llm
    if not args.local_llm:
        selected = available_llms[_llm]
        if selected != "local":
            _llm = selected

    run(args.task, args.input, _llm, args.name, args.n_cqs, args.include_description, args.verbose, args.output,
        args.id, args.local_llm, args.n_examples)
