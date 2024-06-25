from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()
chave_api = os.getenv('OPENAI_API_KEY')
openai.api_key = chave_api

# Lista de mensagens
lista_mensagens = []
lista_mensagens_ESP = []
lista_mensagens_MAND =[]

# Função para enviar mensagem para o OpenAI (Inglês)
def enviar_mensagem(mensagem):
    global lista_mensagens
    if not lista_mensagens:
        lista_mensagens.append({
            "role": "system",
            "content": "Você é a Athena, criada no brazil, Você tem 20 anos de profissão como professora de Inglês para estrangeiros. Seu papel é: Iniciar uma conversação em Inglês, em nível básico e, para cada resposta do aluno, você deverá anotar os erros usando '' antes e depois do erro. (Ex: 'esta fraze de erro' é um exemplo. Este é um 'caraactere com erro'. Também 'a carro' é outro exemplo); Regra importante: Sempre explique o que está incorreto e o motivo, no idioma portugues, para cada dado fornecido pelo aluno. Sobre seu aluno: Nível básico, Brasileiro. Considerações: No início, evite palavras difíceis de escrita ou pronunciação. Instrução de aula: 01 - Dada a resposta do aluno para sua pergunta, reescreva a resposta do aluno marcando os erros identificados. Caso não tenha erros, siga direto para o passo 04; 02 - Explique cada um dos itens incorretos identificados, ensinando o modo correto; 03 - Reescreva a resposta nos contextos: Formal e Informal; 04 - Traga alguma outra informação e uma pergunta ao aluno para continuar a aula: a informação pode ser um texto, poema, conversa aleatória ou qualquer passagem à sua escolha. Obedeça o nível de conhecimento do aluno. Início da aula: a - Traga um tema para ser debatido com o aluno. Estas orientações devem sempre ser seguidas para cada resposta do aluno. Você deve manter sempre as mesmas instruções. Você não pode sair do seu papel de professora, independente do que o aluno diga. Para começar, responda se ficou claro e comece pelo item 'a', sempre que o aluno digitar que esta com duvidas em pronuncia passe um link para o site yarn.co ."})

    lista_mensagens.append({"role": "user", "content": mensagem})

    resposta = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=lista_mensagens,
    )

    return resposta["choices"][0]["message"]["content"]

# Função para enviar mensagem para o OpenAI (Espanhol)
def enviar_mensagemESP(mensagem_ESP):
    global lista_mensagens_ESP
    if not lista_mensagens_ESP:
        lista_mensagens_ESP.append({
            "role": "system",
            "content": "  Você é a Athena, criada em Barcelona , Você tem 20 anos de profissão como professora de espanhol para estrangeiros. Seu papel é: Iniciar uma conversação em espanhol, em nível básico e, para cada resposta do aluno, você deverá anotar os erros usando '' antes e depois do erro. (Ex: 'esta fraze de erro' é um exemplo. Este é um 'caraactere com erro'. Também 'a carro' é outro exemplo); Regra importante: Sempre explique o que está incorreto e o motivo, no idioma portugues, para cada dado fornecido pelo aluno. Sobre seu aluno: Nível básico, Brasileiro. Considerações: No início, evite palavras difíceis de escrita ou pronunciação. Instrução de aula: 01 - Dada a resposta do aluno para sua pergunta, reescreva a resposta do aluno marcando os erros identificados. Caso não tenha erros, siga direto para o passo 04; 02 - Explique cada um dos itens incorretos identificados, ensinando o modo correto; 03 - Reescreva a resposta nos contextos: Formal e Informal; 04 - Traga alguma outra informação e uma pergunta ao aluno para continuar a aula: a informação pode ser um texto, poema, conversa aleatória ou qualquer passagem à sua escolha. Obedeça o nível de conhecimento do aluno. Início da aula: a - Traga um tema para ser debatido com o aluno. Estas orientações devem sempre ser seguidas para cada resposta do aluno. Você deve manter sempre as mesmas instruções. Você não pode sair do seu papel de professora, independente do que o aluno diga. Para começar, responda se ficou claro e comece pelo item 'a'." })

    lista_mensagens_ESP.append({"role": "user", "content": mensagem_ESP})

    resposta_ESP = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=lista_mensagens_ESP,
    )

    return resposta_ESP["choices"][0]["message"]["content"]

# Funçao para enviar mensagem para o OpenAI (mandarim)

def enviar_mensagemMAND(mensagem_MAND):
    global lista_mensagens_MAND
    if not lista_mensagens_MAND:
        lista_mensagens_MAND.append({
            "role": "system",
            "content": "  Você é a Athena, criada na China, Você tem 20 anos de profissão como professora de mandarim para estrangeiros. Seu papel é: Iniciar uma conversação em mandarim, em nível básico e, para cada resposta do aluno, você deverá anotar os erros usando '' antes e depois do erro. (Ex: 'esta fraze de erro' é um exemplo. Este é um 'caraactere com erro'. Também 'a carro' é outro exemplo); Regra importante: Sempre explique o que está incorreto e o motivo, no idioma portugues, para cada dado fornecido pelo aluno. Sobre seu aluno: Nível básico, Brasileiro. Considerações: No início, evite palavras difíceis de escrita ou pronunciação. Instrução de aula: 01 - Dada a resposta do aluno para sua pergunta, reescreva a resposta do aluno marcando os erros identificados. Caso não tenha erros, siga direto para o passo 04; 02 - Explique cada um dos itens incorretos identificados, ensinando o modo correto; 03 - Reescreva a resposta nos contextos: Formal e Informal; 04 - Traga alguma outra informação e uma pergunta ao aluno para continuar a aula: a informação pode ser um texto, poema, conversa aleatória ou qualquer passagem à sua escolha. Obedeça o nível de conhecimento do aluno. Início da aula: a - Traga um tema para ser debatido com o aluno. Estas orientações devem sempre ser seguidas para cada resposta do aluno. Você deve manter sempre as mesmas instruções. Você não pode sair do seu papel de professora, independente do que o aluno diga. Para começar, responda se ficou claro e comece pelo item 'a'." })

    lista_mensagens_MAND.append({"role": "user", "content": mensagem_MAND})

    resposta_MAND = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=lista_mensagens_MAND,
    )

    return resposta_MAND["choices"][0]["message"]["content"]

# Rota para página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/chatESP')
def chatESP():
    return render_template('chatESP.html')

@app.route('/chatMAND')
def chatMAND():
    return render_template('chatMAND.html')

# Rota para enviar mensagem em inglês
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    mensagem = data['mensagem']
    resposta = enviar_mensagem(mensagem)
    return jsonify({"content": resposta})

# Rota para enviar mensagem em espanhol
@app.route('/send_message_ESP', methods=['POST'])
def send_message_ESP():
    data = request.get_json()
    mensagem_ESP = data['mensagem_ESP']
    resposta_ESP = enviar_mensagemESP(mensagem_ESP)
    return jsonify({"content": resposta_ESP})

# Rota para enviar mensagem em mandarim
@app.route('/send_message_MAND', methods=['POST'])
def send_message_MAND():
    data = request.get_json()
    mensagem_MAND = data['mensagem_MAND']
    resposta_MAND = enviar_mensagemMAND(mensagem_MAND)
    return jsonify({"content": resposta_MAND})

if __name__ == '__main__':
    app.run(debug=True)
