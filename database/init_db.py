from database.db import get_connection
from database.schema import TASKS_TABLE


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(TASKS_TABLE)

    conn.commit()
    conn.close()

    print("Database initialized successfully!")