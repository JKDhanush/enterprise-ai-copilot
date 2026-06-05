from llm.service import LLMService

llm = LLMService()


def route_question(question):

    question = question.lower()

    # -------------------
    # SQL ROUTING
    # -------------------

    sql_keywords = [
        "revenue",
        "sales",
        "customer",
        "customers",
        "product",
        "products",
        "trend",
        "analytics",
        "top",
        "highest",
        "lowest",
        "database"
    ]

    if any(
        keyword in question
        for keyword in sql_keywords
    ):
        return "sql"

    # -------------------
    # RAG ROUTING
    # -------------------

    rag_keywords = [
        "resume",
        "cv",
        "document",
        "pdf",
        "experience",
        "skills",
        "project",
        "projects",
        "internship"
    ]

    if any(
        keyword in question
        for keyword in rag_keywords
    ):
        return "rag"

    # -------------------
    # GENERAL
    # -------------------

    return "general"