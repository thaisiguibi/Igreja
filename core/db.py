import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "igreja.db")


DB_PATH = "igreja.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_key = ON")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT
        active INTEGER DEFAULT 1
        )
        """)

    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        active INTEGER DEFAULT 1
        )
        """)

    conn.commit()
    conn.close()
