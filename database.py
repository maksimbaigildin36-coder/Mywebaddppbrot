import sqlite3

db = sqlite3.connect("casino_ultimate.db", check_same_thread=False)
cursor = db.cursor()

# Пользователи
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username TEXT,
nickname TEXT,
balance INTEGER DEFAULT 1000,
banned INTEGER DEFAULT 0
)
""")

# Инвентарь игроков
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory(
user_id INTEGER,
item TEXT,
rarity TEXT
)
""")

db.commit()


def add_user(user_id, username):
    cursor.execute("INSERT OR IGNORE INTO users(id, username) VALUES (?,?)",
                   (user_id, username))
    db.commit()


def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()


def add_balance(user_id, amount):
    cursor.execute("UPDATE users SET balance=balance+? WHERE id=?", (amount, user_id))
    db.commit()


def remove_balance(user_id, amount):
    cursor.execute("UPDATE users SET balance=balance-? WHERE id=?", (amount, user_id))
    db.commit()


def set_nickname(user_id, nickname):
    cursor.execute("UPDATE users SET nickname=? WHERE id=?", (nickname, user_id))
    db.commit()


def ban_user(user_id):
    cursor.execute("UPDATE users SET banned=1 WHERE id=?", (user_id,))
    db.commit()


def unban_user(user_id):
    cursor.execute("UPDATE users SET banned=0 WHERE id=?", (user_id,))
    db.commit()


def add_item(user_id, item, rarity):
    cursor.execute("INSERT INTO inventory(user_id, item, rarity) VALUES(?,?,?)",
                   (user_id, item, rarity))
    db.commit()


def get_inventory(user_id):
    cursor.execute("SELECT item, rarity FROM inventory WHERE user_id=?", (user_id,))
    return cursor.fetchall()


def get_all_users():
    cursor.execute("SELECT id, username, nickname, balance FROM users")
    return cursor.fetchall()