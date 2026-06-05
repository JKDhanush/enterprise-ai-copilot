from llm.openrouter import OpenRouterClient
from llm.groq_client import GroqClient


class LLMService:

    def __init__(self):
        self.openrouter = OpenRouterClient()
        self.groq = GroqClient()

    def generate(
        self,
        messages,
        provider="openrouter"
    ):

        if provider == "groq":
            return self.groq.generate(messages)

        return self.openrouter.generate(messages)