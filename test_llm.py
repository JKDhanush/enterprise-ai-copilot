from llm.service import LLMService

llm = LLMService()

messages = [
    {
        "role": "user",
        "content": "What is LangGraph?"
    }
]

response = llm.generate(messages)

print(response)