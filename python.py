import sqlite3

conn = sqlite3.connect('employees.db')

cursor = conn.cursor()

# Vytvoření tabulky zaměstnanců
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        age INTEGER NOT NULL,
        salary REAL NOT NULL,
        city TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
