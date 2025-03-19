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

# Create a function to remove a book from the database
def remove_book():
    title = input("Enter the title of the book you want to remove: ")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE title = ?", (title))

    conn.commit()
    conn.close()
    print("Book removed successfully!\n")

# Create a function to search books
def search_books():
    choices = input("Search by (1) Title, (2) Author: ")
    search_terms=input("Enter search terms:")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    if choices == "1":
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + search_terms + '%',))
    else:
        cursor.execute("SELECT * FROM books WHERE author LIKE ?", ('%' + search_terms + '%',))
    books = cursor.fetchall()
    conn.close()
    if books:
        for book in books:
            print(f"{book[1]} by {book[2]} ({book[3]}) - {book[4]} - {"Read" if book[5] else "Unread"}")
    else:
        print("No matching books found.\n")

# Create a function to display books
def display_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    if books:
        for book in books:
            print(f"{book[1]} by {book[2]} ({book[3]}) - {book[4]} - {"Read" if book[5] else "Unread"}")
    else:
        print("No books in library.\n")

# Create a function to display statistics for each book in the library
def display_statistics():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT (*) FROM books WHERE read_status = 1")
    read_books = cursor.fetchone()[0]
    conn.close()
    percentag_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total Books: {total_books}")
    print(f" Percentage read: {percentag_read}")

def main():
    create_database()
    while True:
        print("\n Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book")
        print("4. Display all book")
        print("5. Display Statistics")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!\n")
if __name__ == "__main__":
    main()