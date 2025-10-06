# #import sqlite3

# # create a simple SQLite database and a table
# sqlite3.connect('sidds.db')






# # connect to the database
# conn = sqlite3.connect('sidds.db')

# # create a cursor object which allows us to execute SQL commands
# cursor = conn.cursor()

# # create a X with raw sql commands
# cursor.execute('''SELECT * FROM patients''')

# # commit the changes
# conn.commit()

# # close the connection
# conn.close()

import sqlite3

from pathlib import Path

# Paths
db_path = Path(r"C:\Users\siddi\Desktop\PYTHON\health-sqlite-lite\health-sqlite-lite\clinic_simple.db")

schema_path = Path(r"C:\Users\siddi\Desktop\PYTHON\health-sqlite-lite\health-sqlite-lite\sql\schema.sql")

# Connect to DB

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Run schema

with open(schema_path, "r") as f:

    schema_sql = f.read()

cursor.executescript(schema_sql)

conn.commit()

conn.close()

print(" Database created with schema applied")

 