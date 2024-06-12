# Employee Management System Using Python - Sagar Developer

from os import system
import re
# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost", user="admin", password="password", database="company_db")


# Function to Add_Employ
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    employee_id = input("Enter Employee Id: ")

    first_name = input("Enter Employee First Name: ")
    
    last_name = input("Enter Employee Last Name: ")

    mail = input("Enter Employee Email ID: ")

    salary = input("Enter Employee Salary: ")

    project_id = input("Enter Project ID of Employee: ")

    manager_id = input("Enter Manager ID of Employee: ")

    employee_id ,first_name ,last_name ,mail ,salary ,project_id ,manager_id 



    data = (employee_id ,first_name ,last_name ,mail ,salary ,project_id ,manager_id )



    try:
        sql = 'insert into employee values(%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()

        # Executing the sql Query
        c.execute(sql, data)

        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Added Employee Record")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() == "yes":
            Add_Employ()  # Retry the function
        else:
            menu()
    finally:
        press = input("Press Any Key To Continue..")
        menu()


# Function to Add a Project
def Add_Project():
    print("{:>60}".format("-->>Add Project Record<<--"))
    project_id = input("Enter Project ID: ")
    name = input("Enter Project Name: ")
    budget = input("Enter Project Budget: ")
    manager_id = input("Enter Manager ID for the Project: ")
    n_of_employee = input("Enter Number of Employees on the Project: ")

    data = (project_id, name, budget, manager_id, n_of_employee)
    sql = 'INSERT INTO project VALUES (%s, %s, %s, %s, %s)'


    try:
        c = con.cursor()

        # Executing the sql Query
        c.execute(sql, data)

        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Added Employee Record")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() == "yes":
            Add_Employ()  # Retry the function
        else:
            menu()
    finally:
        press = input("Press Any Key To Continue..")
        menu()

# Function to Add a Manager
def Add_Manager():
    print("{:>60}".format("-->>Add Manager Record<<--"))
    manager_id = input("Enter Manager ID: ")
    first_name = input("Enter Manager First Name: ")
    last_name = input("Enter Manager Last Name: ")
    mail = input("Enter Manager Email ID: ")
    salary = input("Enter Manager Salary: ")
    project_id = input("Enter Project ID managed by the Manager: ")

    data = (manager_id, first_name, last_name, mail, salary, project_id)
    sql = 'INSERT INTO manager VALUES (%s, %s, %s, %s, %s, %s)'


    try:
        c = con.cursor()

        # Executing the sql Query
        c.execute(sql, data)

        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Added Employee Record")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        retry = input("Do you want to try again? (yes/no): ")
        if retry.lower() == "yes":
            Add_Employ()  # Retry the function
        else:
            menu()
    finally:
        press = input("Press Any Key To Continue..")
        menu()


# Function to Display Employee Records
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Records <<--"))
    # Query to select all rows from the employee table
    sql = 'SELECT * FROM employee'
    c = con.cursor()

    # Executing the SQL query
    c.execute(sql)

    # Fetching all details of all the Employees
    employees = c.fetchall()
    for employee in employees:
        print("Employee ID:", employee[0])
        print("First Name:", employee[1])
        print("Last Name:", employee[2])
        print("Email:", employee[3])
        print("Salary:", employee[4])
        print("Project ID:", employee[5])
        print("Manager ID:", employee[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()


# Function to Display Project Records
def Display_Project():
    print("{:>60}".format("-->> Display Project Records <<--"))
    # Query to select all rows from the project table
    sql = 'SELECT * FROM project'
    c = con.cursor()

    # Executing the SQL query
    c.execute(sql)

    # Fetching all details of all the Projects
    projects = c.fetchall()
    for project in projects:
        print("Project ID:", project[0])
        print("Name:", project[1])
        print("Budget:", project[2])
        print("Manager ID:", project[3])
        print("Number of Employees:", project[4])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()


# Function to Display Manager Records
def Display_Manager():
    print("{:>60}".format("-->> Display Manager Records <<--"))
    # Query to select all rows from the manager table
    sql = 'SELECT * FROM manager'
    c = con.cursor()

    # Executing the SQL query
    c.execute(sql)

    # Fetching all details of all the Managers
    managers = c.fetchall()
    for manager in managers:
        print("Manager ID:", manager[0])
        print("First Name:", manager[1])
        print("Last Name:", manager[2])
        print("Email:", manager[3])
        print("Salary:", manager[4])
        print("Project ID:", manager[5])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

# Menu function to display menu
def menu():
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Add Project")
    print("4. Display Project Record")
    print("5. Add Manager")
    print("6. Display Manager Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Display_Employ()
    elif ch == 3:
        Add_Project()
    elif ch == 4:
        Display_Project()
    elif ch == 5:
        Add_Manager()
    elif ch == 6:
        Display_Manager()
    elif ch == 7:
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()


# Calling menu function
menu()