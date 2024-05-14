import sqlite3

conn = sqlite3.connect('xxxxxx.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS medicine (id INT, name TEXT, date INT, value INT)')
cursor.execute('''INSERT INTO phch (id, name, date, value)VALUES (0, 'KUPEN', 'CF', 5)''')
cursor.execute('''INSERT INTO students (id, name, faculty, grade)VALUES (1, 'Islom', 'CF', 4)''')
cursor.execute('''UPDATE students SET grade = 5 WHERE id = 1''')
cursor.execute('''SELECT * FROM students''')import sqlite3


conn = sqlite3.connect('xxxxxx.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS medicine (id INT, name TEXT, date INT, value INT)')
cursor.execute('''INSERT INTO phch (id, name, date, value)VALUES (0, 'KUPEN', 'CF', 5)''')
cursor.execute('''INSERT INTO students (id, name, faculty, grade)VALUES (1, 'Islom', 'CF', 4)''')
cursor.execute('''UPDATE students SET grade = 5 WHERE id = 1''')
cursor.execute('''SELECT * FROM students''')
