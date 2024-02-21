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

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "3,2"  # Specify the GPU id
os.environ["HUGGINGFACE_HUB_CACHE"] = "/data/huggingface/"
# device = "cuda"

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B")
model = AutoModelForCausalLM.from_pretrained("yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B",
                                             device_map='sequential', load_in_8bit=True, use_safetensors=True)

# inputs = tokenizer(template, return_tensors="pt")
inputs = tokenizer([template], return_tensors="pt").to('cuda')

outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
