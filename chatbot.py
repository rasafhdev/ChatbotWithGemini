import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API = os.getenv('CHAVE_SECRETA_API_GEMINI')

genai.configure(
    api_key = CHAVE_API
)

modelo_escolhido = genai.GenerativeModel('gemini-pro')
chat = modelo_escolhido.start_chat(history=[])

while True:
    usuario = input('\033[96mVocê: \033[0m')

    if usuario.strip().lower() == 'sair':
        break

    gemini = chat.send_message(usuario)
    print(f'\n\033[95mBot:\033[0m {gemini.text}\n')