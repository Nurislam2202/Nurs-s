import sqlite3
with sqlite3.connect('person.db') as connect:
    cursor = connect.cursor()
    # cursor.execute(''' DROP TABLE IF EXISTS employees''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    employeeID INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    departmentID INTEGER
    )''')

    # cursor.execute(''' DROP TABLE IF EXISTS departments''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS departments(
    departmentID INTEGER,
    departmentName TEXT,
    FOREIGN KEY (departmentID) REFERENCES employees(departmentID)
    )''')

    cursor.execute(''' INSERT INTO departments(departmentID, departmentName) VALUES
        (101, 'HR'),
        (102, 'IT'),
        (103, 'Sales')
    ''')

    cursor.execute(''' SELECT * FROM departments''')
    for i in cursor.fetchall():
        print(i)

    cursor.execute(''' INSERT INTO employees(firstName, lastName, departmentID) VALUES
    ('Nurislam', 'Uraimov', 102),
    ('Marlen', 'Omurbek uulu', 102),
    ('Atabek', 'Esenaliev', 101),
    ('Kudaybergen', 'Urbaev', 101),
    ('Mirbol', 'Kanimetov', 103),
    ('Bekmamat', 'Kadyrov', 103)
    ''')

    cursor.execute(''' SELECT * FROM employees''')
    print('---------------')
    for i in cursor.fetchall():
        print(i)

    cursor.execute(''' SELECT employees.employeeID, employees.firstName, employees.departmentID
    FROM employees
    JOIN departments ON employees.departmentID = departments.departmentID
    ''')
    print('---------------')
    for i in cursor.fetchall():
        print(i)

    cursor.execute(''' SELECT * FROM employees WHERE departmentID = 102''')
    print('---------------')
    for i in cursor.fetchall():
        print(i)
