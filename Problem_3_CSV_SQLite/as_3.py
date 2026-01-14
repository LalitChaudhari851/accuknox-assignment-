import csv
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    email TEXT
)""")

with open("users.csv","r") as file :
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO users VALUES (? , ?)",
            (row[0],row[1])
            
        )
conn.commit()

cursor.execute("SELECT * FROM users")
for user in cursor.fetchall():
    print(user)
    
conn.close()


