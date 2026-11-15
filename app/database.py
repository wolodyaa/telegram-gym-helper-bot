import sqlite3

from config import DB_PATH

def init_db():

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("""

        CREATE TABLE IF NOT EXISTS users(
        user_id integer PRIMARY KEY,
        name text,
        surname text,
        faculty text
        )
        
        """)

def register(user_id: int, name: str, surname: str, faculty: str):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("INSERT OR REPLACE INTO users (user_id, name, surname, faculty) VALUES (?, ?, ?, ?)", (user_id, name, surname, faculty))


def get_reg_data(user_id: int):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("SELECT name FROM users WHERE user_id = ? ORDER BY rowid DESC LIMIT 1", (user_id,))

        result = c.fetchone()

        if result:
            return result[0]
        else:
            return None