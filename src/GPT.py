import os
# get a token: https://platform.openai.com/account/api-keys

from getpass import getpass

OPENAI_API_KEY = os.getenv("key")

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)