import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)
MODEL = "meta-llama/llama-3.1-8b-instruct"

def ask(prompt, temperature):
    resp = client.chat.completions.create(
        model=MODEL,
        max_tokens=100,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()

prompts = [
    "Give me a name for a coffee shop. Reply with just the name.",
    "What is 17 x 23? Reply with just the number.",
]

for p in prompts:
    for t in (0, 1):
        print(f"\n{p} | temperature={t}")
        for i in range(5):
            print(f"  {i+1}: {ask(p, t)}")