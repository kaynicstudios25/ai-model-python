import os
from dotenv import load_dotenv 
from openai import OpenAI 

load_dotenv()  # Load from .env file

client = OpenAI(
    api_key=os.getenv('AI_KEY'),
    base_url=os.getenv('AI_URL')
)

messages = [{
    "role": "user", 
    "content": "Write a one-sentence summary about oddities."
}]

response = client.chat.completions.create(
    model=os.getenv('AI_MODEL'),
    messages=messages
)

print(response.choices[0].message.content)