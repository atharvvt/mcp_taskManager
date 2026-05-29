from mcp_instance import mcp
from database.operations import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task_status,
    delete_task
)


@mcp.tool()
def list_tasks():
    return str(get_tasks())


@mcp.tool()
def add_task(title: str, description: str):
    create_task(title, description)

    return "Task created successfully!"


@mcp.tool()
def list_tasks():
    """
    Get all tasks.
    """

    tasks = get_tasks()

    return [
        {
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "status": task[3],
            "priority": task[4],
            "due_date": task[5],
            "created_at": task[6]
        }
        for task in tasks
    ]


@mcp.tool()
def add_task(title: str, description: str):
    """
    Create a new task.
    """

    create_task(title, description)

    return {
        "success": True,
        "message": "Task created successfully"
    }


@mcp.tool()
def get_task(task_id: int):
    """
    Get task by ID.
    """

    task = get_task_by_id(task_id)

    if not task:
        return {
            "success": False,
            "message": "Task not found"
        }

    return {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "status": task[3],
        "priority": task[4],
        "due_date": task[5],
        "created_at": task[6]
    }


@mcp.tool()
def mark_task_completed(task_id: int):
    """
    Mark task as completed.
    """

    success = update_task_status(
        task_id,
        "completed"
    )

    if not success:
        return {
            "success": False,
            "message": "Task not found"
        }

    return {
        "success": True,
        "message": "Task marked as completed"
    }


@mcp.tool()
def remove_task(task_id: int):
    """
    Delete a task.
    """

    success = delete_task(task_id)

    if not success:
        return {
            "success": False,
            "message": "Task not found"
        }

    return {
        "success": True,
        "message": "Task deleted successfully"
    }