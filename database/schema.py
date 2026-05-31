TASKS_TABLE = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'medium',
    due_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    embedding TEXT
);
"""