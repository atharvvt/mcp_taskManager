import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME)