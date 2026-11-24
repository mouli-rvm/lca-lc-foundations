from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

response = client.responses.create(
  model="gpt-6-astra",
  input="write a haiku about mouli ravilla",
  store=True,
)

print(response.output_text);