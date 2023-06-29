import sqlite3

connection = sqlite3.connect('databse.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users(firstname, lastname, email) VALUES (?, ?, ?)",
            ('john', 'doe', "john@gmail.com")
            )
connection.commit()
print('success')



connection.close()