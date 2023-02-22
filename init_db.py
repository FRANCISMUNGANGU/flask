import sqlite3

# create a connection to a db
# execute the schema script: executescript() : executes multiple sql statements at once
connection = sqlite3.connect("database.db")
with open('schema.sql') as f:
    connection.executescript(f.read())

# set cursor object to be able to navigate rows in table created
# cursor object allows use to process rows in databases
cursor = connection.cursor()
# create dummy content
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First post', 'content first post'))
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second post', 'content second post'))
# commit
connection.commit()
# close
connection.close()
