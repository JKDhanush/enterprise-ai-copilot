import sqlite3
import random
from faker import Faker

fake = Faker()

conn = sqlite3.connect(
    "data/sales.db"
)

cursor = conn.cursor()

cursor.execute(
"""
DROP TABLE IF EXISTS sales
"""
)

cursor.execute(
"""
CREATE TABLE sales(
    sale_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    product_name TEXT,
    revenue REAL,
    sale_date TEXT
)
"""
)

products = [
    "Enterprise AI Copilot",
    "Voice Assistant",
    "Document Intelligence",
    "Analytics Suite",
    "Chat Assistant"
]

for _ in range(1000):

    cursor.execute(
        """
        INSERT INTO sales(
            customer_name,
            product_name,
            revenue,
            sale_date
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            fake.company(),
            random.choice(products),
            round(
                random.uniform(
                    1000,
                    50000
                ),
                2
            ),
            str(
                fake.date_between(
                    start_date="-1y",
                    end_date="today"
                )
            )
        )
    )

conn.commit()
conn.close()

print("Database created.")