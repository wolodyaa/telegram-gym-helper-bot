import sqlite3

from assets.config import DB_PATH

def init_db():

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("""
        
        CREATE TABLE IF NOT EXISTS users(
        user_id integer PRIMARY KEY,
        name text,
        surname text,
        study_group text

        )""")

def register(user_id: int, name: str, surname: str, study_group: str):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("INSERT OR REPLACE INTO users (user_id, name, surname, study_group) VALUES (?, ?, ?, ?)", (user_id, name, surname, study_group))


def get_reg_data(user_id: int):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("SELECT name FROM users WHERE user_id = ? ORDER BY rowid DESC LIMIT 1", (user_id,))

        result = c.fetchone()

        if result:
            return result[0]
        else:
            return None


def delete_data(user_id: int):

    with sqlite3.connect(DB_PATH) as db:

        c = db.cursor()

        c.execute("DELETE FROM users WHERE user_id = ?", (user_id,))