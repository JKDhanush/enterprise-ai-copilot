from llm.service import LLMService

llm = LLMService()


def route_question(question):

    messages = [
        {
            "role": "system",
            "content": """
You are a routing agent.

Classify the user query into exactly ONE category.

sql
rag
general

sql:
- revenue
- sales
- products
- customers
- analytics
- database

rag:
- uploaded documents
- resumes
- candidate evaluation
- skills
- experience
- projects
- document summaries

general:
- everything else

Return ONLY one word:
sql
rag
general
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    route = llm.generate(
        messages,
        provider="groq"
    )

    route = route.strip().lower()

    if route not in [
        "sql",
        "rag",
        "general"
    ]:
        route = "general"

    return route