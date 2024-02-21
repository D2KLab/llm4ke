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

from pathlib import Path

import yaml


# === Functions ===============================================================

class LocalTemplate:
    """
    A class for handling prompting templates
    """

    input = None

    def __init__(self, body, _input):
        """
        Class constructor
        :param body: the template as a string
        :param _input: the set of parameters of the template
        """
        self.body = body
        self.input = _input

    def __str__(self):
        return "Template body = {0}".format(self.body)

    def get(self):
        """
        Get the template body
        :return: template body as a string
        """
        return self.body

    @classmethod
    def load(self, input_path):
        """
        Load a template from a file and make a LocalTemplate instance with it.
        :param input_path: file path to a YAML template
        :return: a LocalTemplate instance
        """
        t_config = yaml.safe_load(Path(input_path).read_text())

        body = t_config['Body']
        for k, v in t_config.get('Import', {}).items():
            body = body.replace('{%s}' % k, Path(v).read_text())

        return LocalTemplate(body, t_config['Input'])
