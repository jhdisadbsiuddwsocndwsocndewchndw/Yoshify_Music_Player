import sqlite3

# connects to the database file called yoshify.db
# if the file doesn't already exist, sqlite creates it automatically
connection = sqlite3.connect("yoshify.db")

# creates a cursor, which is used to run SQL commands on the database
cursor = connection.cursor()

# creates a table called "users" if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

connection.commit()

def addUser(username, password):
    # inserts a new row into the users table with the given username and password
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )
    # saves the new user permanently to the database file
    connection.commit()


def checkUser(username, password):
    # searches the users table for a row where both the username and password match
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    # gets the first matching row found, or None if there was no match
    user = cursor.fetchone()

    if user:
        return True
    
    else:
        return False
