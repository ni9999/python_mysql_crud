from os import system
import re
import mysql.connector

# Making Connection
con = mysql.connector.connect(
    host="localhost", user="admin", password="password", database="libraryDB"
)

# Function to Add a Book
def Add_Book():
    print("{:>60}".format("-->>Add Book Record<<--"))
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    genre = input("Enter Book Genre: ")

    data = (title, author, genre)
    sql = 'INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)'

    try:
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Successfully Added Book Record")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() == "yes":
            Add_Book()
        else:
            menu()
    finally:
        input("Press Any Key To Continue..")
        menu()

# Function to Add a Borrower
def Add_Borrower():
    print("{:>60}".format("-->>Add Borrower Record<<--"))
    name = input("Enter Borrower Name: ")
    address = input("Enter Borrower Address: ")
    phone_number = input("Enter Borrower Phone Number: ")
    email = input("Enter Borrower Email: ")

    data = (name, address, phone_number, email)
    sql = 'INSERT INTO borrowers (name, address, phone_number, email) VALUES (%s, %s, %s, %s)'

    try:
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Successfully Added Borrower Record")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() == "yes":
            Add_Borrower()
        else:
            menu()
    finally:
        input("Press Any Key To Continue..")
        menu()

# Function to Add a Transaction
def Add_Transaction():
    print("{:>60}".format("-->>Add Transaction Record<<--"))
    book_id = input("Enter Book ID: ")
    borrower_id = input("Enter Borrower ID: ")
    borrow_date = input("Enter Borrow Date (YYYY-MM-DD): ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD, leave blank if not returned): ")

    data = (book_id, borrower_id, borrow_date, due_date, return_date if return_date else None)
    sql = 'INSERT INTO transactions (book_id, borrower_id, borrow_date, due_date, return_date) VALUES (%s, %s, %s, %s, %s)'

    try:
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Successfully Added Transaction Record")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() == "yes":
            Add_Transaction()
        else:
            menu()
    finally:
        input("Press Any Key To Continue..")
        menu()

# Function to Display Books
def Display_Books():
    print("{:>60}".format("-->> Display Book Records <<--"))
    sql = 'SELECT * FROM books'
    c = con.cursor()
    c.execute(sql)
    books = c.fetchall()
    for book in books:
        print("Book ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Genre:", book[3])
        print("\n")
    input("Press Any key To Continue..")
    menu()

# Function to Display Borrowers
def Display_Borrowers():
    print("{:>60}".format("-->> Display Borrower Records <<--"))
    sql = 'SELECT * FROM borrowers'
    c = con.cursor()
    c.execute(sql)
    borrowers = c.fetchall()
    for borrower in borrowers:
        print("Borrower ID:", borrower[0])
        print("Name:", borrower[1])
        print("Address:", borrower[2])
        print("Phone Number:", borrower[3])
        print("Email:", borrower[4])
        print("\n")
    input("Press Any key To Continue..")
    menu()

# Function to Display Transactions
def Display_Transactions():
    print("{:>60}".format("-->> Display Transaction Records <<--"))
    sql = 'SELECT * FROM transactions'
    c = con.cursor()
    c.execute(sql)
    transactions = c.fetchall()
    for transaction in transactions:
        print("Transaction ID:", transaction[0])
        print("Book ID:", transaction[1])
        print("Borrower ID:", transaction[2])
        print("Borrow Date:", transaction[3])
        print("Due Date:", transaction[4])
        print("Return Date:", transaction[5])
        print("\n")
    input("Press Any key To Continue..")
    menu()

# Menu function to display menu
def menu():
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Library Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Book")
    print("2. Display Book Record")
    print("3. Add Borrower")
    print("4. Display Borrower Record")
    print("5. Add Transaction")
    print("6. Display Transaction Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Book()
    elif ch == 2:
        Display_Books()
    elif ch == 3:
        Add_Borrower()
    elif ch == 4:
        Display_Borrowers()
    elif ch == 5:
        Add_Transaction()
    elif ch == 6:
        Display_Transactions()
    elif ch == 7:
        print("{:>60}".format("Have A Nice Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        input("Press Any key To Continue..")
        menu()

# Calling menu function
menu()
