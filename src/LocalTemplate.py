import os
import yaml
from pathlib import Path
from langchain_community.graphs import RdfGraph
from langchain_core.prompts.prompt import PromptTemplate


class LocalTemplate():
    def __init__(self, body, input):
        self.body = body
        self.input = input

    def get(self):
        # print(self.body)
        return self.body

    @classmethod
    def load(self, input_path):
        t_config = yaml.safe_load(Path(input_path).read_text())

        body = t_config['Body']
        for k, v in t_config.get('Import', {}).items():
            # g = RdfGraph(
            #     source_file=v,
            #     standard="rdf",
            #     local_copy=os.path.join('temp', k),
            # )

            body = body.replace('{%s}' % k, Path(v).read_text()) #g.get_schema)

        return LocalTemplate(body, t_config['Input'])
