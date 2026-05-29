from database.db import get_connection
from database.schema import TASKS_TABLE


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(TASKS_TABLE)

    conn.commit()
    conn.close()


def create_task(title, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
        """,
        (title, description)
    )

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

    cursor.execute(
        """
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """,
        (status, task_id)
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