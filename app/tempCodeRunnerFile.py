import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash


conn = sqlite3.Connection('data/profes.db')

c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT NOT NULL,
            admin BOOLEAN
        )
        ''')

conn.commit()

# password = 'admin'
# hash_pw= generate_password_hash(password)

c.execute('UPDATE users SET admin="1" WHERE username="Estevet"')

conn.commit()
conn.close()
