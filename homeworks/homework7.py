import sqlite3 as sql

with sql.connect('homework.db') as connection:
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(15) NOT NULL,
        surname VARCHAR(15) NOT NULL,
        year_of_birth INTEGER,
        hobby VARCHAR(30),
        homework_points INTEGER
    )''')
    cursor.execute(''' INSERT INTO student (name, surname, year_of_birth, hobby, homework_points)
    VALUES
        ('Fatima', 'Danielbekova', 2006, 'books', 10),
	    ('Nurislam', 'Uraimov', 2004, 'football', 8),
	    ('Atabek', 'Esenaliev', 2003, 'geography', 10),
	    ('Kudaybergen', 'Urbaev', 2004, 'chess', 9),
	    ('Aisha', 'Asanova', 2001, 'cooking', 10),
	    ('Marlen', 'Janyshbekov', 2003, 'books', 8),
	    ('Mirbol', 'Qarbekov', 2003, 'football', 10),
	    ('Bekmamat', 'Ulanov', 2004, 'business', 10),
	    ('Amina', 'Usonova', 2004, 'math', 10),
	    ('Aibek', 'Qamchybekov', 2003, 'cars', 8)
    ''')
    cursor.execute(''' SELECT * FROM student WHERE surname > 10 ''')
    cursor.execute(''' UPDATE student SET name = 'genius' WHERE homework_points = 10 ''')
    cursor.execute(''' SELECT * FROM student WHERE name = 'genius' ''')
    for i in cursor.fetchall():
        print(i)
    cursor.execute(''' DELETE FROM student WHERE id % 2 = 0 ''')
