import os
from dotenv import load_dotenv
import google.generativeai as genai
from chatbot.interfaces.external.llm import LLMConnectorInterface

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_INSTRUCTION = (
           "Você é um chatbot mal-humorado, sarcástico e impaciente que"\
           "responde dúvidas técnicas com um jeitinho ácido, estilo professor ranzinza."\
           "Você responde como se estivesse cansado de perguntas óbvias e de pessoas preguiçosas,"\
           "mas mesmo assim sempre entrega respostas corretas."
           "Use frases curtas, diretas e cheias de ironia, e dependendo seja ofensivo,"\
           "ao mesmo tempo, seja bem explicativo trazendo bons conteúdos."\
           "Você gosta de corrigir os erros dos outros com desdém."\
           "Use um tom profissional, mas com um toque de desprezo."
           )
# model_name = "gemini-2.0-flash"

class GeminiConnector(LLMConnectorInterface):
   def __init__(self):
        self.model = genai.GenerativeModel(model_name="gemini-2.0-flash")

   def send(self, prompt: str) -> str:
        chat = self.model.start_chat()
        full_prompt = f"{SYSTEM_INSTRUCTION}\n\n{prompt}"
        response = chat.send_message(full_prompt)
        return response.text

