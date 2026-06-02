import json
from database.db import get_connection
from database.schema import TASKS_TABLE
from services.embedding_service import embedding_to_json, generate_embedding
from datetime import datetime, timedelta, date


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

def update_task(
    task_id,
    title=None,
    description=None,
    priority=None,
    due_date=None
):
    conn = get_connection()
    cursor = conn.cursor()

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

    current_title = task[1]
    current_description = task[2]
    current_status = task[3]
    current_priority = task[4]
    current_due_date = task[5]

    due_date = (
    due_date
    if due_date is not None
    else current_due_date
    )

    title = title if title is not None else current_title
    description = (
        description
        if description is not None
        else current_description
    )
    priority = (
        priority
        if priority is not None
        else current_priority
    )

    task_text = f"""
    Task Title: {title}
    Task Description: {description}
    Status: {current_status}
    Priority: {priority}
    """

    embedding = generate_embedding(task_text)

    cursor.execute(
        """
        UPDATE tasks
        SET
            title = ?,
            description = ?,
            priority = ?,
            due_date = ?,
            embedding = ?
        WHERE id = ?
        """,
        (
            title,
            description,
            priority,
            due_date,
            json.dumps(embedding),
            task_id
        )
    )

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows > 0

def rebuild_embeddings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        """
    )

    tasks = cursor.fetchall()

    updated_count = 0

    for task in tasks:

        task_id = task[0]

        task_text = f"""
        Task Title: {task[1]}
        Task Description: {task[2]}
        Status: {task[3]}
        Priority: {task[4]}
        """

        embedding = generate_embedding(
            task_text
        )

        cursor.execute(
            """
            UPDATE tasks
            SET embedding = ?
            WHERE id = ?
            """,
            (
                json.dumps(embedding),
                task_id
            )
        )

        updated_count += 1

    conn.commit()
    conn.close()

    return updated_count

def get_task_statistics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        """
    )
    total_tasks = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'completed'
        """
    )
    completed_tasks = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'pending'
        """
    )
    pending_tasks = cursor.fetchone()[0]

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100,
            2
        )

    conn.close()

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_rate": completion_rate
    }

def get_tasks_by_priority():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT priority,
               COUNT(*)
        FROM tasks
        GROUP BY priority
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return {
        priority: count
        for priority, count in rows
    }

def get_tasks_by_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT status,
               COUNT(*)
        FROM tasks
        GROUP BY status
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return {
        status: count
        for status, count in rows
    }

def get_tasks_due_today():
    today = date.today().isoformat()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE due_date = ?
        """,
        (today,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def get_overdue_tasks():
    today = date.today().isoformat()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE due_date < ?
        AND status != 'completed'
        """,
        (today,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def get_tasks_due_this_week():
    today = datetime.today().date()

    end_date = today + timedelta(days=7)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE due_date BETWEEN ? AND ?
        """,
        (
            today.isoformat(),
            end_date.isoformat()
        )
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def calculate_task_score(task):

    score = 0

    priority = task[4]
    due_date = task[5]
    status = task[3]

    # Ignore completed tasks
    if status == "completed":
        return 0

    # Priority weight
    if priority == "high":
        score += 50

    elif priority == "medium":
        score += 30

    elif priority == "low":
        score += 10

    # Due date weight
    if due_date:

        today = datetime.today().date()

        due = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).date()

        days_remaining = (
            due - today
        ).days

        if days_remaining < 0:
            score += 50

        elif days_remaining == 0:
            score += 40

        elif days_remaining <= 3:
            score += 30

        elif days_remaining <= 7:
            score += 20

        else:
            score += 10

    return score

def prioritize_tasks():

    tasks = get_tasks()

    ranked = []

    for task in tasks:

        score = calculate_task_score(
            task
        )

        if score == 0:
            continue

        ranked.append(
            (score, task)
        )

    ranked.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked

def generate_cluster_name(tasks):

    titles = " ".join(
        task["title"]
        for task in tasks
    )

    return titles[:50]