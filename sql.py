import sqlite3


conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Create Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER,
    Hire_Date TEXT
    )
    ''')

    # Create Departments table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Manager TEXT
    )
    ''')

    # Insert data into Employees table
cursor.executemany('''
    INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date)
    VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 'Alice', 'Sales', 50000, '2021-01-15'),
        (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
        (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
    ])

    # Insert data into Departments table
cursor.executemany('''
    INSERT INTO Departments (ID, Name, Manager)
    VALUES (?, ?, ?)
    ''', [
        (1, 'Sales', 'Alice'),
        (2, 'Engineering', 'Bob'),
        (3, 'Marketing', 'Charlie')
    ])

conn.commit()
conn.close()

