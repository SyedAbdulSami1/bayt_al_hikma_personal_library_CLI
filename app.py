import sqlite3      # Import sqlite3 module

# Create a function to create a database
def create_database():
    conn= sqlite3.connect("library.db") # creating "library.db" database 
    cursor = conn.cursor()      # connecting to the database connection #Creating a table in database
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS books (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    year INTEGER,
                    genre TEXT,
                    read BOOLEAN
     )               
    """)
    #save changes to
    conn.commit() # commit yo Dsb4 changes 
    conn.close() # close the connection

# Create a function to add a book to the database
def add_book():
    title = input("Enter Book Title: " )
    author = input ("Enter Book Author: ")
    year = int(input("Enter Book year: "))
    genre = input ("Enter Genere: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, genre, read_status) VALUES (?, ?, ?, ?, ?)", 
                   (title, author, year, genre, read_status))
    conn.commit()
    conn.close()
    print("Book added successfully!\n")