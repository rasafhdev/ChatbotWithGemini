import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(
    api_key = API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    question = input('Você: ')

    if question.strip().lower() == 'sair':
        break

    response = chat.send_message(question)
    print(f'\nBot: {response.text}\n')