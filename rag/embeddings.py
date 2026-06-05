from openai import OpenAI

from config.settings import OPENROUTER_API_KEY


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def get_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    
    return response.data[0].embedding