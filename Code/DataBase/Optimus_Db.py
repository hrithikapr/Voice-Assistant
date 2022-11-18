import sqlite3

conn = sqlite3.connect("Optimus.db")

c = conn.cursor()

if(conn):
    c.execute('''CREATE TABLE Contact(
        name TEXT,
        phno INTEGER
    )''')
    print("Table created successfully")

conn.commit()

conn.close()
