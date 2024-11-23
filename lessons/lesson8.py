import sqlite3 as sql

with sql.connect('games.db') as conn:
    cursor = conn.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS users''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL
    )''')

    # cursor.execute(''' DROP TABLE IF EXISTS games''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS games(
    game_id INTEGER PRIMARY KEY,
    game_name TEXT NOT NULL,
    timeit INTEGER,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
    )''')

    # cursor.execute(''' INSERT INTO users(username) VALUES
    # ('beka'), ('bob'), ('alisa'), ('michael'), ('jack')
    # ''')

    cursor.execute(''' SELECT * FROM users''')
    for i in cursor.fetchall():
        print(i)

    # cursor.execute(''' INSERT INTO games(game_name, timeit, user_id) VALUES
    # ('LOL', 2, 1)
    # ''')

    cursor.execute(''' SELECT * FROM games''')
    print('--------------------')
    for i in cursor.fetchall():
        print(i)

    cursor.execute(''' SELECT users.user_id, users.username, games.game_id, games.timeit
    FROM users
    JOIN games ON users.user_id = games.game_id
    ''')
    print('--------------------')
    for i in cursor.fetchall():
        print(i)
