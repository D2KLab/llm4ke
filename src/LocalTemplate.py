import os
import yaml
from pathlib import Path
from langchain_community.graphs import RdfGraph
from langchain_core.prompts.prompt import PromptTemplate


class LocalTemplate:
    input = None

    def __init__(self, body, _input):
        self.body = body
        self.input = _input

    def get(self):
        # print(self.body)
        return self.body

    @classmethod
    def load(self, input_path):
        t_config = yaml.safe_load(Path(input_path).read_text())

        body = t_config['Body']
        for k, v in t_config.get('Import', {}).items():
            body = body.replace('{%s}' % k, Path(v).read_text())

        return LocalTemplate(body, t_config['Input'])
