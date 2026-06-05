from openai import OpenAI

from config.settings import OPENROUTER_API_KEY


class OpenRouterClient:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY
        )

    def generate(
        self,
        messages,
        model="deepseek/deepseek-chat-v3-0324",
        temperature=0.3
    ):

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content