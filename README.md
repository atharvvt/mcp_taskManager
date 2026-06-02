# MCP AI Task Manager

An AI-powered task management system built with Python, SQLite, Sentence Transformers, FAISS, and the Model Context Protocol (MCP).

This project exposes a local task management database as MCP tools, allowing AI assistants such as Claude Desktop to create, search, prioritize, cluster, and manage tasks using natural language.

Unlike traditional task managers, this system supports semantic search, vector embeddings, intelligent recommendations, and AI-driven task analysis.

---

# Features

## Core Task Management

* Create tasks
* Update tasks
* Delete tasks
* Mark tasks as completed
* Search tasks by keyword
* Filter pending and completed tasks
* Due date management
* Priority management

## AI Features

### Semantic Search

Search tasks by meaning rather than exact keywords.

Example:

```text
Find tasks related to machine learning
```

Returns relevant tasks even if they do not contain the exact words used in the query.

---

### Vector Embeddings

Every task is automatically converted into a vector embedding using:

```text
Sentence Transformers
all-MiniLM-L6-v2
```

Embeddings are stored directly inside SQLite.

---

### FAISS Vector Search

Task retrieval is accelerated using Facebook AI Similarity Search (FAISS).

Benefits:

* Fast similarity search
* Scalable retrieval
* Vector indexing
* Production-style architecture

---

### Related Task Recommendations

Find tasks that are semantically similar.

Example:

```text
Show tasks related to semantic search
```

Useful for identifying duplicate work and grouping related projects.

---

### Task Clustering

Automatically groups tasks into semantic categories using KMeans clustering.

Example output:

```text
Cluster 1
- Learn MCP
- Research semantic search

Cluster 2
- Buy fishing bait
- Buy peanuts

Cluster 3
- Go karting
- Go fishing
```

---

### Smart Prioritization

Tasks are ranked using:

* Priority
* Due date
* Completion status

This enables AI assistants to recommend the most important work first.

---

# Architecture

```text
Claude Desktop
        ↓
Model Context Protocol
        ↓
Python MCP Server
        ↓
Task Tools
        ↓
SQLite Database
        ↓
Stored Embeddings
        ↓
FAISS Vector Index
```

---

# Tech Stack

## Backend

* Python
* SQLite

## AI / ML

* Sentence Transformers
* FAISS
* NumPy
* Scikit-Learn

## Agent Layer

* MCP Python SDK
* Claude Desktop

---

# Project Structure

```text
└── 📁mcp_app
    └── 📁__pycache__
        ├── main.cpython-314.pyc
        ├── mcp_instance.cpython-314.pyc
        ├── server.cpython-314.pyc
    └── 📁config
        ├── __init__.py
    └── 📁database
        └── 📁__pycache__
            ├── __init__.cpython-314.pyc
            ├── db.cpython-314.pyc
            ├── init_db.cpython-314.pyc
            ├── operations.cpython-314.pyc
            ├── schema.cpython-314.pyc
        └── 📁migrations
            └── 📁__pycache__
                ├── migrate_embeddings.cpython-314.pyc
                ├── migrations.cpython-314.pyc
            ├── migrate_embeddings.py
            ├── migrations.py
        ├── __init__.py
        ├── db.py
        ├── init_db.py
        ├── models.py
        ├── operations.py
        ├── schema.py
    └── 📁models
        ├── __init__.py
    └── 📁services
        └── 📁__pycache__
            ├── __init__.cpython-314.pyc
            ├── cluster_tasks.cpython-314.pyc
            ├── embedding_service.cpython-314.pyc
            ├── embeddings.cpython-314.pyc
            ├── faiss_service.cpython-314.pyc
            ├── find_related_tasks.cpython-314.pyc
            ├── semantic_search.cpython-314.pyc
        ├── __init__.py
        ├── cluster_tasks.py
        ├── embedding_service.py
        ├── faiss_service.py
        ├── find_related_tasks.py
        ├── semantic_search.py
    └── 📁tests
    └── 📁tools
        └── 📁__pycache__
            ├── __init__.cpython-314.pyc
            ├── task_tools.cpython-314.pyc
        ├── __init__.py
        ├── task_tools.py
    ├── main.py
    ├── mcp_instance.py
    ├── README.md
    ├── requirements.txt
    ├── server.py
    └── tasks.db
```

---

# Available MCP Tools

## Task Management

* add_task
* list_tasks
* get_task
* update_task
* remove_task
* mark_task_completed

## Search

* search_task
* semantic_search_tasks

## Analytics

* recommend_related_tasks
* group_tasks_by_topic
* get_task_priorities

## Productivity

* list_pending_tasks
* list_completed_tasks
* list_tasks_due_today
* list_tasks_due_this_week
* list_overdue_tasks

---

# Example Queries

```text
Create a task to learn retrieval augmented generation
```

```text
Find tasks related to AI infrastructure
```

```text
What should I work on first?
```

```text
Group my tasks by topic
```

```text
Show overdue tasks
```

```text
Recommend related work
```

---

# Key Engineering Concepts Demonstrated

* MCP Server Development
* AI Tool Engineering
* Semantic Search
* Vector Embeddings
* FAISS Indexing
* Recommendation Systems
* Clustering Algorithms
* SQLite Database Design
* AI Agent Integration
* Local-First AI Systems

---

# Resume Description

Built an AI-powered task management system using Python, SQLite, Sentence Transformers, FAISS, and the Model Context Protocol (MCP). Implemented semantic search, vector retrieval, task clustering, prioritization, recommendation systems, and AI-agent tooling for natural language task management.

---

# Future Improvements

* Local LLM Integration (Ollama)
* Retrieval-Augmented Generation (RAG)
* ChromaDB Support
* LanceDB Support
* Automatic Task Categorization
* AI Daily Planning Assistant
* Multi-user Support

---

# Author

Atharv

Computer Science Student

Interests:

* AI Engineering
* Developer Tools
* Generative AI
* Local AI Systems
* Machine Learning Infrastructure
