from llm.service import LLMService

llm = LLMService()


def route_question(question):

    messages = [
        {
            "role": "system",
            "content": """
You are a routing agent.

Classify the user query into ONE category:

sql
rag
voice

Rules:

sql:
- sales
- revenue
- customers
- products
- analytics
- database questions

rag:
- uploaded documents
- resumes
- PDFs
- candidate evaluation
- skills
- projects
- experience
- summaries

voice:
- call recordings
- transcripts
- sentiment
- action items
- customer support calls

Return ONLY one word:

sql
rag
voice
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

    return route.strip().lower()