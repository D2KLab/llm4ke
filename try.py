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
