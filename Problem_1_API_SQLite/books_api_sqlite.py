import requests 
import sqlite3

url ="https://openlibrary.org/subjects/programming.json?limit=10"
response = requests.get(url)
data = response.json()

books = data["works"]

conn = sqlite3.connect("books.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    title TEXT,
    author TEXT,
    year INTEGER
)              
""")

for book in books :
    title = book.get("title","N/A")
    author = book["authors"][0]["name"] if book.get("authors") else "Unknown"
    year = book.get("first_publish_year",0)
    
    cursor.execute(
        "INSERT INTO books VALUES (?,?,?)",
        (title,author,year)
    )

conn.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)
    
conn.close()