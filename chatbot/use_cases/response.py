from chatbot.interfaces.external.llm import LLMConnectorInterface

class GetResponseUseCase:
    def __init__(self, llm_connector: LLMConnectorInterface):
        self.llm_connector = llm_connector

    def execute(self, pergunta: str) -> str:
        response = self.llm_connector.send(pergunta)
        return response