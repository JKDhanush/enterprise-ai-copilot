from rag.retriever import retrieve

from llm.service import LLMService


llm = LLMService()


def answer_question(question):

    chunks = retrieve(question)

    context = "\n\n".join(chunks)

    messages = [
        {
            "role": "system",
            "content": f"""
Use the provided context.

Context:
{context}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    answer = llm.generate(messages)

    return answer, chunks