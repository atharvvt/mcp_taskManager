# MCP Task Manager

An AI-native task management system built using the Model Context Protocol (MCP), SQLite, and Python.

This project exposes a local task management database as MCP tools, allowing AI assistants like Claude Desktop to autonomously interact with tasks using natural language.

---

# Features

* MCP server built using Python
* SQLite-based persistent task storage
* AI tool integration with Claude Desktop
* CRUD task operations
* Task search and filtering
* Agent-friendly structured responses
* Modular backend architecture
* Local-first architecture
* Foundation for semantic search and AI workflows

---

# Architecture

```text
Claude Desktop
      ↓
MCP Protocol
      ↓
Python MCP Server
      ↓
Tool Layer
      ↓
SQLite Database
```

---

# Tech Stack

## Backend

* Python
* SQLite
* MCP Python SDK

## AI / Agent Layer

* Claude Desktop
* Model Context Protocol (MCP)

## Upcoming AI Features

* Sentence Transformers
* Semantic Search
* Local Embeddings
* Ollama / Gemma Integration

---

# Project Structure

```text
mcp_app/
│
├── database/
│   ├── db.py
│   ├── models.py
│   ├── operations.py
│   └── schema.py
│
├── tools/
│   └── task_tools.py
│
├── services/
│   └── embedding_service.py
│
├── server.py
├── tasks.db
├── README.md
└── requirements.txt
```

---

# MCP Tools

The server exposes multiple AI-callable tools.

## Available Tools

### list_tasks

Retrieve all tasks.

---

### add_task

Create a new task.

Parameters:

* title
* description

---

### get_task

Retrieve task by ID.

Parameters:

* task_id

---

### mark_task_completed

Mark a task as completed.

Parameters:

* task_id

---

### remove_task

Delete a task.

Parameters:

* task_id

---

### search_task

Search tasks using keywords.

Parameters:

* keyword

---

### list_pending_tasks

Retrieve all pending tasks.

---

### list_completed_tasks

Retrieve all completed tasks.

---

# Database Schema

## tasks table

| Column      | Type      |
| ----------- | --------- |
| id          | INTEGER   |
| title       | TEXT      |
| description | TEXT      |
| status      | TEXT      |
| priority    | TEXT      |
| due_date    | TEXT      |
| created_at  | TIMESTAMP |

---

# Installation

## Clone Repository

```bash
git clone <your_repo_url>
cd mcp_app
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the MCP Server

```bash
python server.py
```

---

# Running MCP Inspector

Install MCP CLI:

```bash
pip install "mcp[cli]"
```

Run Inspector:

```bash
mcp dev server.py
```

---

# Claude Desktop Integration

Add the following configuration inside:

```text
claude_desktop_config.json
```

```json
{
  "mcp_servers": {
    "task-manager": {
      "command": "B:\\mcp_app\\.venv\\Scripts\\python.exe",
      "args": [
        "B:\\mcp_app\\server.py"
      ]
    }
  }
}
```

Restart Claude Desktop after saving.

---

# Example Claude Interactions

```text
Show all my tasks
```

```text
Create a task to learn semantic search
```

```text
Complete the first task
```

```text
Remove duplicate tasks
```

---

# Current Capabilities

* Persistent local task management
* AI-controlled CRUD workflows
* Local tool invocation through MCP
* Multi-step AI reasoning using tools
* Agent-friendly tool architecture

---

# Future Roadmap

## Semantic Search

Use embeddings for meaning-based task retrieval.

Example:

```text
Find tasks related to backend optimization
```

---

## Offline AI Integration

Integrate local LLMs using:

* Ollama
* Gemma
* Llama.cpp

---

## AI Planning System

Allow AI agents to:

* prioritize tasks
* summarize work
* generate daily plans
* automate workflows

---

## Vector Database Support

Potential future integrations:

* ChromaDB
* FAISS
* LanceDB

---

# Why This Project Matters

This project demonstrates:

* AI tooling infrastructure
* MCP protocol implementation
* Backend architecture design
* AI-agent interaction patterns
* Local-first AI systems
* Structured tool engineering

This aligns closely with modern AI engineering workflows used in tools like Cursor, Claude Desktop, and AI agent frameworks.

---

# Learning Outcomes

Through this project I learned:

* MCP server development
* AI tool integration
* SQLite database architecture
* Tool-driven AI workflows
* Agent-friendly API design
* Semantic retrieval concepts
* Local AI infrastructure patterns

---

# Author

Atharv

Computer Science student focused on:

* AI Engineering
* Developer Tooling
* Generative AI
* Local AI Systems
* Game Development

---
