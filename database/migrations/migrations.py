# database/migrations.py

from database.db import get_connection

def add_embedding_column():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE tasks
        ADD COLUMN embedding TEXT
    """)

    conn.commit()
    conn.close()