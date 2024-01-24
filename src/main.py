import os
import re
from argparse import ArgumentParser
from langchain_community.llms import Ollama
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from rdflib import Graph, RDF, RDFS, OWL

from LocalTemplate import LocalTemplate


def simplify(uri):
    return re.split(r'[#/]', uri)[-1].replace('_', ' ')


def run(task, input, llm_model, ont_name):
    llm = Ollama(model=llm_model)

    os.makedirs('temp', exist_ok=True)

    g = Graph()
    g.parse(input, format='n3')

    cls = [s for s, p, o in g.triples((None, RDF.type, OWL.Class))]
    props = ([s for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty))] +
             [s for s, p, o in g.triples((None, RDF.type, OWL.DatatypeProperty))])

    ont_input = {'name': ont_name,
                 'n': 10,
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

    res = chain.invoke(input_dict)

    print(res)


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='LLM4ke',
        description='Experiment about LLMs on Knowledge Graphs')
    parser.add_argument('task', choices=['all_classes', 'all_classes+properties', 'logic'])
    parser.add_argument('-i', '--input', help='Input ontology', default='./dm-rdf/Odeuropa/odeuropa-ontology.owl')
    parser.add_argument('--llm', help='LLM to use', default='llama2')
    parser.add_argument('--name', help='Name of the ontology', required=True)
    args = parser.parse_args()
    run(args.task, args.input, args.llm, args.name)
