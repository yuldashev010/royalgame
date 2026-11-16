
import sqlite3

DB_NAME = "royalgame.db"


def connect():
    return sqlite3.connect(DB_NAME)


def init_db():
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            coins INTEGER DEFAULT 5,
            level INTEGER DEFAULT 1,
            wins INTEGER DEFAULT 0,
            losses INTEGER DEFAULT 0
        )
    """)

    db.commit()
    db.close()


def create_user(user_id, username):
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users
        (user_id, username, coins)
        VALUES (?, ?, 5)
    """, (user_id, username))

    db.commit()
    db.close()


def get_user(user_id):
    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()
    db.close()

    return user


def add_coins(user_id, amount):
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE users
        SET coins = coins + ?
        WHERE user_id = ?
    """, (amount, user_id))

    db.commit()
    db.close()


def init():
    init_db()
  
