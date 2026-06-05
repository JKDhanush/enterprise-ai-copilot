from openai import OpenAI

from config.settings import GROQ_API_KEY


class GroqClient:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=GROQ_API_KEY
        )

    def generate(
        self,
        messages,
        model="openai/gpt-oss-120b",
        temperature=0.3
    ):

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content