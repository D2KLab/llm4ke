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


def simplify(uri):
    return re.split(r'[#/]', uri)[-1].replace('_', ' ')


class CustomHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        formatted_prompts = "\n".join(prompts)
        print(f"********** Prompt **************\n{formatted_prompts}\n********** End Prompt **************")


def run(task, input_path, llm_model, ont_name, n_cqs=10, include_description=False, verbose=False, output_path='/out', id=None):
    llm = Ollama(model=llm_model)

    # os.makedirs('temp', exist_ok=True)

    g = Graph()
    for g_path in os.listdir(path.join(input_path, 'dm')):
        if not g_path.split('.')[-1] in ['rdf', 'ttl', 'owl']:
            continue
        g.parse(path.join(input_path, 'dm', g_path))

    cls = [s for s, p, o in g.triples((None, RDF.type, OWL.Class))]
    props = ([s for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty))] +
             [s for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty))])

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
    print(ont_input['schema'])

    PROMPT_TEMPLATE = LocalTemplate.load(f'./src/prompt_templates/{task}.yml')

    sparql_prompt = PromptTemplate(
        input_variables=["prompt"] + PROMPT_TEMPLATE.input, template=PROMPT_TEMPLATE.get()
    )

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
    parser = ArgumentParser(
        prog='LLM4ke',
        description='Experiment about LLMs on Knowledge Graphs')
    parser.add_argument('task', choices=['all_classes', 'all_classes+properties', 'logic'])
    parser.add_argument('-i', '--input', help='Input folder', default='./data/Odeuropa/')
    parser.add_argument('-o', '--output', help='Output folder', default='./out/')
    parser.add_argument('--llm', help='LLM to use', default='llama2')
    parser.add_argument('--name', help='Name of the ontology', required=True)
    parser.add_argument('-n', '--n_cqs', help='Number of competency questions to get in output', default=10)
    parser.add_argument('--include_description', help='Include the content of description.txt in the prompt',
                        default=False, action='store_true')
    parser.add_argument('--verbose', help='Print the full prompt',
                        default=False, action='store_true')
    parser.add_argument('--id', help='Id for naming the output file. If absent, it will be a timestamp')

    args = parser.parse_args()
    run(args.task, args.input, args.llm, args.name, args.n_cqs, args.include_description, args.verbose, args.output, args.id)
