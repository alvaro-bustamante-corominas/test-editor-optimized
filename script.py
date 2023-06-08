import openai
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

openai.api_key = os.getenv("API_KEY")

while True:

  prompt = input("\n Enter a question: ")

  if prompt == "exit":
    break

  respuesta = openai.Completion.create(engine="ada",
                    prompt = prompt,
                    max_tokens=2048)

  print(respuesta.choices[0].text)