from agents.sql_agent import (
    answer_sql_question
)

sql, result = answer_sql_question(
    "Show top 5 customers by revenue"
)

print(sql)

print(result.head())