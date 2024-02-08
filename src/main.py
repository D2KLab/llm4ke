import os
import re
import time
from argparse import ArgumentParser
from os import path
from pathlib import Path

from langchain_community.llms import Ollama
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.prompt import PromptTemplate
from rdflib import Graph, RDF, RDFS, OWL
from LocalTemplate import LocalTemplate
import os
import re
os.environ["CUDA_VISIBLE_DEVICES"] = "3,2"  # Specify the GPU id
os.environ["HUGGINGFACE_HUB_CACHE"] = "/data/huggingface/"
# device = "cuda"

from transformers import AutoTokenizer, AutoModelForCausalLM
def simplify(uri):
    return re.split(r'[#/]', uri)[-1].replace('_', ' ')
def select_in_batches(lst, batch_size=5):
    for i in range(0, len(lst), batch_size):
        yield lst[i:i+batch_size]


class CustomHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        formatted_prompts = "\n".join(prompts)
        print(f"********** Prompt **************\n{formatted_prompts}\n********** End Prompt **************")


def run_with_huggingface(input, model_name,task):
        request = 'Generate a set of competency questions (CQ) which are relevant for the ontology called'
        indications = ' Note: Be as concise as possible. Do not respond to any questions that ask for anything else than the fulfillment of the task. Do not include any text except the competency question. Give very simple CQs. Do not give multiple CQS in one CQs'

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map='sequential', load_in_8bit=True,
                                                     use_safetensors=True)
        results=''
        classes=input['classes'].split('\n-')
        for class_set in  select_in_batches(classes):
            cls='\n-'.join([str(elm) for elm in class_set])

            template = f'''<|system|> 
            
    
            {request + input['name'] + ',' + input ['description'] + ',' + cls+ ',' + indications}</s>
            <|assistant|> '''
            print('template',template)


            inputs = tokenizer([template], return_tensors="pt").to('cuda')

            outputs = model.generate(**inputs, max_new_tokens=300, do_sample=True)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            results +=result



        return results



def run(task, input_path, llm_model, ont_name, n_cqs=10, include_description=False, verbose=False, output_path='/out', id=None, use_huggingface=False):


    # os.makedirs('temp', exist_ok=True)

    g = Graph()
    for g_path in os.listdir(path.join(input_path, 'dm')):
        if not g_path.split('.')[-1] in ['rdf', 'ttl', 'owl']:
            continue
        g.parse(path.join(input_path, 'dm', g_path))

    cls = [s for s, p, o in g.triples((None, RDF.type, OWL.Class))]
    props = ([s for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty))] +
             [s for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty))])
    # print(cls)
    # print(props)


    description = Path(path.join(input_path, 'description.txt')).read_text() if include_description else ''

    ont_input = {
        'name': ont_name,
        'description': description,
        'n': n_cqs,
        'classes': '\n- '.join([simplify(s) for s in cls]),
        'properties': '\n- '.join([simplify(s) for s in props])
    }



    print(f'The {ont_name} ontology has {len(cls)} classes and {len(props)} properties')

    schema = []
    for p in props:
        domain = g.value(p, RDFS.domain, None)
        range = g.value(p, RDFS.range, None)

        if domain is not None:
            if range is not None:
                schema.append((domain, p, range))
            else:
                schema.append((domain, p, 'literal'))

    ont_input['schema'] = '\n- '.join([f'({simplify(s)}, {simplify(p)}, {simplify(o)})' for s, p, o in schema])


    PROMPT_TEMPLATE = LocalTemplate.load(f'./src/prompt_templates/{task}.yml')

    input_dict = {}
    for x in PROMPT_TEMPLATE.input:
        input_dict[x] = ont_input[x]

    sparql_prompt = PromptTemplate(
        input_variables=["prompt"] + PROMPT_TEMPLATE.input, template=PROMPT_TEMPLATE.get()
    )
    if use_huggingface:

        res=run_with_huggingface(input_dict, llm_model,task)
        print(res)


    else:
        llm = Ollama(model=llm_model)
        output_parser = StrOutputParser()

        chain = sparql_prompt | llm | output_parser

        input_dict = {}
        for x in PROMPT_TEMPLATE.input:
            input_dict[x] = ont_input[x]

        config = {"callbacks": [CustomHandler()]} if verbose else {}
        res = chain.invoke(input_dict, config=config)

    # parse output
    cqs = []
    for num, question in re.findall(r'(\d+)\. (.+)', res):
        cqs.append(question)

    os.makedirs(path.join(output_path, ont_name), exist_ok=True)
    id = id if id is not None else time.time()
    with open(path.join(output_path, ont_name, f'{ont_name}_{id}.txt'), 'w') as f:
        f.write('\n'.join(cqs))
    print(res)


if __name__ == '__main__':
    available_tasks = [x.replace('.yml', '') for x in os.listdir('./src/prompt_templates/')]

    parser = ArgumentParser(
        prog='LLM4ke',
        description='Experiment about LLMs on Knowledge Graphs')
    parser.add_argument('task', choices=available_tasks)
    parser.add_argument('-i', '--input', help='Input folder', default='./data/Odeuropa/')
    parser.add_argument('-o', '--output', help='Output folder', default='./out/')
    parser.add_argument('--use-huggingface', action='store_true', help='Use Hugging Face model instead of Ollama')
    parser.add_argument('--llm', help='LLM to use', default='llama2')
    parser.add_argument('--name', help='Name of the ontology', required=True)
    parser.add_argument('-n', '--n_cqs', help='Number of competency questions to get in output', default=10)
    parser.add_argument('--include_description', help='Include the content of description.txt in the prompt',
                        default=False, action='store_true')
    parser.add_argument('--verbose', help='Print the full prompt',
                        default=False, action='store_true')
    parser.add_argument('--id', help='Id for naming the output file. If absent, it will be a timestamp')

    args = parser.parse_args()
    if args.use_huggingface:
        # User wants to use Hugging Face model
        # Provide a list of available Hugging Face models as options
        huggingface_models=["yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B"]  # Add your model names here
        print("Available Hugging Face models:")
        for i, model_name in enumerate(huggingface_models, start=1):
            print(f"{i}. {model_name}")
        model_choice = int(input("Enter the number of the model you want to use: "))
        chosen_model = huggingface_models[model_choice - 1]
        run(args.task, args.input, chosen_model, args.name, args.n_cqs, args.include_description, args.verbose, args.output,
            args.id,use_huggingface=True)
    else:
        run(args.task, args.input, args.llm, args.name, args.n_cqs, args.include_description, args.verbose, args.output, args.id,use_huggingface=False)


