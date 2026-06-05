from llm.service import LLMService

llm = LLMService()


def summarize_document(text):

    messages = [
        {
            "role": "system",
            "content": """
Summarize this document.

Provide:
- Document Type
- Key Topics
- Main Highlights

Keep under 100 words.
"""
        },
        {
            "role": "user",
            "content": text[:4000]
        }
    ]

    return llm.generate(
        messages,
        provider="groq"
    )