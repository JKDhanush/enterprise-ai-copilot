from llm.service import LLMService
from database.db import run_query

llm = LLMService()

SCHEMA = """

Table: sales

Columns:

sale_id
customer_name
product_name
revenue
sale_date

"""

def generate_sql(question):

    messages = [
        {
            "role": "system",
            "content": f"""
Convert the user's question
into SQLite SQL.

Return ONLY SQL.

Schema:

{SCHEMA}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    return llm.generate(
        messages,
        provider="groq"
    )

def answer_sql_question(question):

    sql = generate_sql(question)

    sql = (
        sql
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    result = run_query(sql)

    return sql, result