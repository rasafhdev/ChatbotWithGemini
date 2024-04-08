# Bem-Vindos! Por favor, leia!

### Chatbot com API Google Gemini
Este projeto me desafiou bastante, pois nunca havia usado uma API. Embora eu já tivesse pleno entendimento do que é API, consegui usar pela primeira vez. Foi um desafio. Inicialmente, meu intuito era criar um código com o ChatGPT-4, pois em um dos cursos que fiz a proposta era essa. Porém, encontrei muitas dificuldades com os parâmetros da OpenAI, inúmeros erros, além também de ser pago.

Após algumas horas, tive a ideia de tentar fazer com o Google e deu certo! Claro, foi necessário pesquisar tudo novamente, focando no Gemini. O mais legal nisso tudo foi encontrar a biblioteca Dotenv, que serve para esconder a chave da API. Ou seja, o código fica à disposição em sua plataforma preferida, e com o Dotenv no arquivo .gitignore, você protege sua chave da API.

Confira o vídeo do programa funcionando! Abaixo do vídeo, existe um guia de como gerar a sua chave do API Gemini.

[chatbot.webm](https://github.com/rasafhdev/ChatbotWithGemini/assets/139464196/3e931f59-5292-4eeb-8334-246a97e72453)

# Guia para API Gemini
1) Baixe meu repositório clonando-o, ou copie o código.
2) Abre o terminal na pasta do seu projeto.
* Crie sua venv (copie e cole):
```
# Linux <3 ou MAC:
python3 -m venv venv 

# Windows:
python -m venv venv
```
* Ative sua VENV:
```
# Linux <3 ou MAC:
source venv/bin/activate
# ou
. venv/bin/activate

# Para Windows:
.\venv\scripts\activate
``` 
* Instale as Libs (todos os sistemas):
```
pip install -r requiriments.txt
```
1) Acesse: https://aistudio.google.com/app/u/0/apikey
2) Crie sua chave (Creat API Key) e guarde-a!
3) Na sua pasta do projeto, crie o arquivo .env (Precisa ser exatamente assim .env)
4) Abra o arquivo .env e crie uma variavel conforme abaixo:
```
CHAVE_SECRETA_API_GEMINI = 'COLE_SUA_CHAVE_API_AQUI'
```
5) Execute o programa :D
