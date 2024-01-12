import os
from argparse import ArgumentParser
from langchain_community.llms import Ollama
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.graphs import RdfGraph
from pathlib import Path

from LocalTemplate import LocalTemplate

def run(task, input):
    llm = Ollama(model="llama2")

    os.makedirs('temp', exist_ok=True)

    # input_graph = RdfGraph(
    #     source_file="./dm-rdf/Odeuropa/odeuropa-ontology.owl",
    #     standard="rdf",
    #     local_copy="test.ttl",
    # )

    input_graph = Path(input).read_text()

    PROMPT_TEMPLATE = LocalTemplate.load(f'./src/prompt_templates/{task}.yml')

    sparql_prompt = PromptTemplate(
        input_variables=["schema", "prompt"], template=PROMPT_TEMPLATE.get()
    )

    output_parser = StrOutputParser()

    chain = sparql_prompt | llm | output_parser

    res = chain.invoke({"schema": input_graph})

    print(res)


if __name__ == '__main__':
    parser = ArgumentParser(
                        prog='LLM4ke',
                        description='Experiment about LLMs on Knowledge Graphs')
    parser.add_argument('task', choices='generate_cqs')
    parser.add_argument('-i', '--input', help='Input ontology', default='./dm-rdf/Odeuropa/odeuropa-ontology.owl')
    args = parser.parse_args()
    run(args.task, args.input)