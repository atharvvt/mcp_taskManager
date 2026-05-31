from database.operations import add_task
from database.operations import get_tasks

task_id = add_task(
    "Build MCP Integration",
    "Connect Claude Desktop to MCP server"
)

print(get_tasks()[-1])