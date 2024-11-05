from dotenv import load_dotenv
import openai
import os
import sys

load_dotenv('.env', override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key = openai_api_key)

os.system('clear')

def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {
            "role": "user",
            "content": prompt
          }
        ],
    temperature=0
    )
    response = completion.choices[0].message.content
    return response
while True:
    prompt = input('Prompt: ')
    with open('gpt_output.txt', 'a') as file:
        file.write(f"Prompt: {prompt}\n")
        response = get_llm_response(prompt)
        file.write(f"Response: {response}\n")
        print(f"Response: {response}")
        file.flush()

