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


# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Data 10 zaměstnanců
employees_data = [
    ('Jan Novák', 'Vývojář', 30, 50000, 'Praha'),
    ('Petr Svoboda', 'Analytik', 25, 45000, 'Brno'),
    ('Karel Dvořák', 'Projektový manažer', 35, 60000, 'Ostrava'),
    ('Anna Novotná', 'Tester', 28, 40000, 'Praha'),
    ('Lucie Kovářová', 'Personalista', 32, 47000, 'Plzeň'),
    ('Tomáš Král', 'IT podpora', 26, 38000, 'Brno'),
    ('Eva Zelená', 'Marketingový specialista', 29, 42000, 'Olomouc'),
    ('Filip Horák', 'Produktový manažer', 31, 52000, 'Hradec Králové'),
    ('Veronika Černá', 'Účetní', 34, 46000, 'Karlovy Vary'),
    ('Michal Procházka', 'Grafik', 27, 43000, 'Zlín')
]

# Hromadné vložení záznamů
cursor.executemany('''
    INSERT INTO employees (name, position, age, salary, city)
    VALUES (?, ?, ?, ?, ?)
''', employees_data)

conn.commit()

conn.close()


