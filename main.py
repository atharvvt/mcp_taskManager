from database.operations import (
    initialize_database,
    create_task,
    get_tasks
)

initialize_database()

create_task(
    "Learn MCP",
    "Build MCP project"
)

print(get_tasks())