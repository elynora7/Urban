import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000)
    ''')
    connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    return products

def is_included(username):
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.commit()
    return True if user else False

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (username, email, age,))
    connection.commit()
    return 'Регистрация прошла успешно'
