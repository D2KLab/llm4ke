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

import os
import wandb
from openai import OpenAI

# === Init ====================================================================

client = OpenAI()
gpt_assistant_prompt = "You are a " + input ("Who should I be, as I answer your prompt?")
gpt_user_prompt = input ("What prompt do you want me to do?")
gpt_prompt = gpt_assistant_prompt, gpt_user_prompt
print(gpt_prompt)
message=[{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": gpt_user_prompt}]
temperature=0.2
max_tokens=256
frequency_penalty=0.0

# === Functions ===============================================================

response = client.chat.completions.create(
    model="gpt-4",
    messages = message,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty
)
print(response.choices[0].message)
wandb.init()
response_text = response.choices[0].message.content
tokens_used = response.usage.total_tokens


prediction_table = wandb.Table(columns=["Prompt", "Response", "Tokens", "Max Tokens", "Frequency Penalty", "Temperature"])
prediction_table.add_data(gpt_prompt, response_text, tokens_used, max_tokens, frequency_penalty, temperature)
wandb.log({'predictions': prediction_table})
wandb.finish()
