import json

from database.operations import get_tasks
from database.db import get_connection
from services.embeddings import generate_embedding


tasks = get_tasks()


print(tasks[0])
print(len(tasks[0]))

conn = get_connection()
cursor = conn.cursor()

for task in tasks:

    if task[7]:
        continue

    task_text = f"""
    Task Title: {task[1]}
    Task Description: {task[2]}
    Status: {task[3]}
    Priority: {task[4]}
    """

    embedding = generate_embedding(task_text)

    cursor.execute(
        """
        UPDATE tasks
        SET embedding = ?
        WHERE id = ?
        """,
        (
            json.dumps(embedding),
            task[0]
        )
    )

conn.commit()
conn.close()

print("Embeddings migrated successfully.")