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

# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Výběr zaměstnanců z Prahy
cursor.execute('SELECT * FROM employees WHERE city = "Praha"')
prague_employees = cursor.fetchall()

# Výpis zaměstnanců
for employee in prague_employees:
    print(employee)

# Zavření připojení
conn.close()

# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

requested_city = "Praha"  

# Výběr zaměstnanců z Prahy mladších než 40 let
cursor.execute('SELECT * FROM employees WHERE city = ? AND age < 40', (requested_city,))
young_employees = cursor.fetchall()

# Výpis zaměstnanců
for employee in young_employees:
    print(employee)

conn.close()

# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Výběr zaměstnanců z Prahy s platem vyšším než 50 000 CZK
cursor.execute('SELECT * FROM employees WHERE city = "Praha" AND salary > 50000')
high_salary_employees = cursor.fetchall()

# Výpis zaměstnanců
for employee in high_salary_employees:
    print(employee)

conn.close()

# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Výběr zaměstnanců z Brna nebo Ostravy starších než 35 a mladších než 45
cursor.execute('''
    SELECT * FROM employees
    WHERE (city = "Brno" OR city = "Ostrava") AND age > 35 AND age < 45
''')
specific_age_employees = cursor.fetchall()

# Výpis zaměstnanců
for employee in specific_age_employees:
    print(employee)


conn.close()

# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Výběr všech zaměstnanců a zobrazení pouze jména, pozice a platu
cursor.execute('SELECT name, position, salary FROM employees')
all_employees = cursor.fetchall()

# Výpis zaměstnanců
for employee in all_employees:
    print(employee)

conn.close()

# Připojení k databázi
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Aktualizace pozice Anny Novotné
cursor.execute('''
    UPDATE employees
    SET position = "Projektový manažer"
    WHERE name = "Anna Novotná"
''')

conn.commit()

# Výpis záznamu Anny Novotné po aktualizaci
cursor.execute('SELECT * FROM employees WHERE name = "Anna Novotná"')
anna_record = cursor.fetchone()
print(anna_record)

# Zavření připojení
conn.close()






