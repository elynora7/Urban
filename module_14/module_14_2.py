import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

cursor.execute("DELETE FROM Users")
cursor.execute("UPDATE SQLITE_SEQUENCE SET seq=0 WHERE name='Users'")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance=? WHERE id=?", (500, i))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = {}".format(i))

cursor.execute("SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
sum = cursor.fetchone()[0]

print(f'{sum / count}')

connection.commit()
connection.close()
