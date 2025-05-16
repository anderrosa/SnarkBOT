from abc import ABC, abstractmethod

class LLMConnectorInterface(ABC):
    @abstractmethod
    def send(self, pergunta: str) -> str:
        """Envia a pergunta para o modelo e retorna a resposta."""
        pass