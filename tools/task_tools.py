from mcp_instance import mcp
from database.operations import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task_status,
    delete_task,
    get_pending_tasks,
    get_completed_tasks,
    search_tasks,
    add_task
    )
from services.embedding_service import semantic_search

def format_task(task):
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
def add_task(title: str, description: str):
    task_id = add_task(title, description)

    return {
        "success": True,
        "task_id": task_id
    }

@mcp.tool()
def list_tasks():
    tasks = get_tasks()
    return [format_task(task) for task in tasks]


@mcp.tool()
def add_task_tool(
    title: str,
    description: str
):
    task_id = add_task(
        title,
        description
    )

    return {
        "success": True,
        "task_id": task_id,
        "message": "Task created successfully"
    }

@mcp.tool()
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if not task:
        return {
            "success": False,
            "message": "Task not found"
        }

    return format_task(task)

@mcp.tool()
def mark_task_completed(task_id: int):
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


@mcp.tool()
def list_pending_tasks():
    tasks = get_pending_tasks()

    return [format_task(task) for task in tasks]


@mcp.tool()
def list_completed_tasks():
    tasks = get_completed_tasks()

    return [format_task(task) for task in tasks]


@mcp.tool()
def search_task(keyword: str):
    tasks = search_tasks(keyword)

    return [format_task(task) for task in tasks]

@mcp.tool()
def semantic_search_tasks(
    query: str
):
    tasks = get_tasks()

    results = semantic_search(tasks,query)

    formatted = []

    for score, task in results:

        formatted.append(
            {
                "id": task[0],
                "title": task[1],
                "description": task[2],
                "status": task[3],
                "priority": task[4],
                "similarity": round(
                    float(score),
                    4
                )
            }
        )

    return formatted