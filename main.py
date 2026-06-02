from database.operations import (
    initialize_database,
    get_tasks,
    add_task
)

initialize_database()
            
add_task(
    "Learn MCP",
    "Build MCP project"
)

print(get_tasks())