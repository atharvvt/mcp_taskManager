# Installation and Setup Guide

This guide explains how to install, configure, and run the MCP AI Task Manager locally.

---

# Prerequisites

Before starting, ensure you have:

* Python 3.11+
* Git
* Claude Desktop (optional, for MCP integration)

Verify Python installation:

```bash
python --version
```

---

# Clone the Repository

```bash
git clone https://github.com/<your-username>/mcp-ai-task-manager.git

cd mcp-ai-task-manager
```

---

# Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
python -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Initialize Database

Run:

```bash
python server.py
```

This automatically creates:

```text
tasks.db
```

if it does not already exist.

---

# Database Migration

If upgrading from an older version of the project:

```bash
python -m database.migrations.migrate_embeddings
```

This adds and populates task embeddings for semantic search.

Expected output:

```text
Embeddings migrated successfully.
```

---

# Running the MCP Server

Start the server:

```bash
python server.py
```

Expected output:

```text
Starting MCP Task Manager Server...
```

---

# Claude Desktop Configuration

Open Claude Desktop configuration file.

Example:

```json
{
  "mcpServers": {
    "task-manager": {
      "command": "python",
      "args": [
        "-m",
        "server"
      ],
      "cwd": "B:/mcp_app"
    }
  }
}
```

Replace:

```text
B:/mcp_app
```

with your project directory.

Restart Claude Desktop after saving the configuration.

---

# Verify MCP Connection

Inside Claude Desktop, try:

```text
List all tasks
```

or

```text
Create a task to learn MCP
```

If configured correctly, Claude will call your MCP tools.

---

# Running Tests

Semantic search test:

```bash
python -m tests.semantic_test
```

Custom test file:

```bash
python -m tests.test
```

---

# Rebuilding Embeddings

If embeddings become outdated:

```text
Use MCP Tool:
rebuild_task_embeddings
```

or run the migration script again:

```bash
python -m database.migrations.migrate_embeddings
```

---

# Rebuilding the FAISS Index

If new tasks are added manually or embeddings are modified:

```text
Use MCP Tool:
rebuild_vector_index
```

This regenerates the FAISS vector index used for semantic search.

---

# Common Issues

## Circular Import Error

Example:

```text
ImportError:
cannot import name ...
from partially initialized module
```

Solution:

* Move imports inside functions when two modules depend on each other.
* Avoid importing `database.operations` globally inside service modules.

---

## Missing Embeddings

Example:

```text
IndexError: tuple index out of range
```

Cause:

```text
Database schema has not been migrated.
```

Fix:

```bash
python -m database.migrations.migrate_embeddings
```

---

## FAISS Not Returning Results

Rebuild the index:

```text
rebuild_vector_index
```

or restart the MCP server.

---

# Stopping the Server

Press:

```text
CTRL + C
```

in the terminal running the server.

---

# Project Components

```text
SQLite Database
    ↓
Task Operations
    ↓
Embeddings
    ↓
FAISS Vector Index
    ↓
MCP Tools
    ↓
Claude Desktop
```

The project is now ready for AI-powered task management using semantic search and MCP.
