import sqlite3

# Query to fetch all data


def showAll():
    conn = sqlite3.connect("Optimus.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM Contact")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

# Query to fetch single phno


def showPhno(name):
    conn = sqlite3.connect("Optimus.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM Contact WHERE name = (?)", (name,))
    items = c.fetchall()

    for item in items:
        return (item[2])

    conn.commit()
    conn.close()

# Add new record


def addOne(name, phno):
    conn = sqlite3.connect("Optimus.db")
    c = conn.cursor()
    c.execute("INSERT INTO Contact VALUES (?,?)", (name, phno))
    conn.commit()
    conn.close()

# Delete record from table


def deleteOne(name):
    conn = sqlite3.connect("Optimus.db")
    c = conn.cursor()
    c.execute("DELETE FROM Contact WHERE name = (?)", (name,))
    conn.commit()
    conn.close()
