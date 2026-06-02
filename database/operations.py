import json

from database.db import get_connection
from database.schema import TASKS_TABLE
from services.embedding_service import embedding_to_json, generate_embedding



def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(TASKS_TABLE)

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    conn.close()

    return task


def update_task_status(task_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    # Get current task
    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    )

    task = cursor.fetchone()

    if not task:
        conn.close()
        return False

    title = task[1]
    description = task[2]
    priority = task[4]

    # Generate updated embedding
    task_text = f"""
    Task Title: {title}
    Task Description: {description}
    Status: {status}
    Priority: {priority}
    """

    embedding = generate_embedding(task_text)

    cursor.execute(
        """
        UPDATE tasks
        SET status = ?,
            embedding = ?
        WHERE id = ?
        """,
        (
            status,
            json.dumps(embedding),
            task_id
        )
    )

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows > 0


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    deleted_rows = cursor.rowcount

    conn.close()

    return deleted_rows > 0


def get_pending_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'pending'
        """
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def get_completed_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE status = 'completed'
        """
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def search_tasks(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE title LIKE ?
        OR description LIKE ?
        """,
        (f"%{keyword}%", f"%{keyword}%")
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def add_task(
    title,
    description,
    status="pending",
    priority="medium"
):
    conn = get_connection()
    cursor = conn.cursor()


    task_text = f"""
    Task Title: {title}
    Task Description: {description}
    Status: {status}
    Priority: {priority}
    """

    embedding = generate_embedding(task_text)

    cursor.execute("""
        INSERT INTO tasks
        (
            title,
            description,
            status,
            priority,
            embedding
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        description,
        status,
        priority,
        embedding_to_json(embedding)
    ))

    task_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return task_id

def clear_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks")

    conn.commit()
    conn.close()