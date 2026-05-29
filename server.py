from mcp_instance import mcp

from database.operations import initialize_database

initialize_database()

from tools.task_tools import *


if __name__ == "__main__":
    mcp.run()