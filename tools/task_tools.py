from mcp_instance import mcp
from database.operations import (
    get_overdue_tasks,
    get_tasks,
    get_task_by_id,
    get_tasks_due_this_week,
    get_tasks_due_today,
    prioritize_tasks,
    update_task_status,
    delete_task,
    get_pending_tasks,
    get_completed_tasks,
    search_tasks,
    add_task as add_task_db,
    clear_tasks,
    update_task,
    rebuild_embeddings,
    get_task_statistics,
    get_tasks_by_priority,
    get_tasks_by_status,
    generate_cluster_name,
    )
from services.cluster_tasks import cluster_tasks
from services.find_related_tasks import (
    find_related_tasks
)
from services.faiss_service import build_faiss_index
from services.semantic_search import semantic_search

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
    task_id = add_task_db(title, description)
    build_faiss_index()

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

    results = semantic_search(query)

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

@mcp.tool()
def clear_all_tasks():
    tasks = get_tasks()

    for task in tasks:
        clear_tasks(task[0])

    return {
        "success": True,
        "message": "All tasks cleared"
    }

@mcp.tool()
def update_task_tool(
    task_id: int,
    title: str = None,
    description: str = None,
    priority: str = None,
    due_date: str = None
):
    success = update_task(
        task_id,
        title,
        description,
        priority,
        due_date
    )

    if not success:
        return {
            "success": False,
            "message": "Task not found"
        }
    
    build_faiss_index()

    return {
        "success": True,
        "message": "Task updated successfully"
    }

@mcp.tool()
def rebuild_task_embeddings():

    updated = rebuild_embeddings()

    build_faiss_index()

    return {
        "success": True,
        "tasks_reindexed": updated
    }

@mcp.tool()
def task_statistics():
    return get_task_statistics()

@mcp.tool()
def tasks_by_priority():
    return get_tasks_by_priority()

@mcp.tool()
def tasks_by_status():
    return get_tasks_by_status()

@mcp.tool()
def suggest_related_tasks(
    task_id: int
):
    target_task = get_task_by_id(
        task_id
    )

    if not target_task:
        return {
            "success": False,
            "message": "Task not found"
        }

    tasks = get_tasks()

    results = find_related_tasks(
        target_task,
        tasks
    )

    recommendations = []

    for score, task in results:

        recommendations.append({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "similarity": round(
                float(score),
                4
            )
        })

    return {
        "task": target_task[1],
        "recommendations": recommendations
    }

@mcp.tool()
def list_tasks_due_today():
    tasks = get_tasks_due_today()

    return [
        format_task(task)
        for task in tasks
    ]

@mcp.tool()
def list_overdue_tasks():
    tasks = get_overdue_tasks()

    return [
        format_task(task)
        for task in tasks
    ]

@mcp.tool()
def list_tasks_due_this_week():
    tasks = get_tasks_due_this_week()

    return [
        format_task(task)
        for task in tasks
    ]

@mcp.tool()
def get_task_priorities():
    ranked_tasks = prioritize_tasks()

    results = []

    for score, task in ranked_tasks:

        results.append({
            "id": task[0],
            "title": task[1],
            "status": task[3],
            "priority": task[4],
            "due_date": task[5],
            "score": score
        })

    return results

@mcp.tool()
def group_tasks_by_topic(
    num_clusters: int = 3
):
    return cluster_tasks(
        num_clusters
    )

@mcp.tool()
def generate_cluster_name_tool(
    cluster_tasks: list
):
    return generate_cluster_name(
        cluster_tasks
    )

@mcp.tool()
def rebuild_vector_index():

    success = build_faiss_index()

    return {
        "success": success
    }