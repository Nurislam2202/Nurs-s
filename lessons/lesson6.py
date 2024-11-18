# database - база данных
# SQL - язык
# СУБД - система управления базами данных

import sqlite3 as sq

with sq.connect('base.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
    fullname TEXT NOT NULL,
    old DATE
)''')
    cursor.execute('''SELECT rowid,fullname,old FROM user  ''')
    print(cursor.fetchall())
