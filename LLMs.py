import os

os.environ["CUDA_VISIBLE_DEVICES"] = "3"  # Specify the GPU id
os.environ["HUGGINGFACE_HUB_CACHE"] = "/data/huggingface/"
# # Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
# tokenizer = AutoTokenizer.from_pretrained("yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B")
# model = AutoModelForCausalLM.from_pretrained("yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B")


# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("fblgit/UNA-TheBeagle-7b-v1")
model = AutoModelForCausalLM.from_pretrained("fblgit/UNA-TheBeagle-7b-v1")

text = "Hello my name is"
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
