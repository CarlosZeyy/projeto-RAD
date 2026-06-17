import sqlite3

def connection():
    conn = sqlite3.connect("my_db.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
''')
    
    conn.commit()

    return conn