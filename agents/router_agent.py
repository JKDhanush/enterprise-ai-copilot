from llm.service import LLMService

llm = LLMService()


def route_question(question):

    messages = [
        {
            "role": "system",
            "content": """
You are a routing agent.

Return ONLY one word.

Valid outputs:

sql
rag
general

No explanation.
No punctuation.
No extra text.
"""
        },
        {
            "role": "user",
            "content": f"""
Question:

{question}

Route:
"""
        }
    ]

    route = llm.generate(
        messages,
        provider="groq"
    )

    route = route.lower()

    if "sql" in route:
        return "sql"

    if "rag" in route:
        return "rag"

    return "general"