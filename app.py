from flask import Flask, request, jsonify, send_from_directory
from chatbot.frameworks_drivers.gemini_connector import GeminiConnector
from chatbot.use_cases.response import GetResponseUseCase
import os

app = Flask(__name__, static_folder="frontend", static_url_path="")

# Instanciando seu conector e use case, respeitando a injeção de dependência
llm_connector = GeminiConnector()
use_case = GetResponseUseCase(llm_connector)

# Servir o index.html ao acessar a raiz "/"
@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

# Servir arquivos estáticos (CSS, JS etc.)
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("frontend", filename)

# Rota da API que recebe mensagem e retorna resposta do bot
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    pergunta = data.get("mensagem", "")
    resposta = use_case.execute(pergunta)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
