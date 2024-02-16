import wandb
from openai import OpenAI

client = OpenAI()
gpt_assistant_prompt = "You are a " + input("Who should I be, as I answer your prompt?")
gpt_user_prompt = input("What prompt do you want me to do?")
gpt_prompt = gpt_assistant_prompt, gpt_user_prompt
print(gpt_prompt)
message = [{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": gpt_user_prompt}]
temperature = 0.2
max_tokens = 256
frequency_penalty = 0.0

response = client.chat.completions.create(
    model="gpt-4",
    messages=message,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty
)
print(response.choices[0].message)
wandb.init()
response_text = response.choices[0].message.content
tokens_used = response.usage.total_tokens

prediction_table = wandb.Table(
    columns=["Prompt", "Response", "Tokens", "Max Tokens", "Frequency Penalty", "Temperature"])
prediction_table.add_data(gpt_prompt, response_text, tokens_used, max_tokens, frequency_penalty, temperature)
wandb.log({'predictions': prediction_table})
wandb.finish()
