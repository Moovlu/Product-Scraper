# Import required modules
import sqlite3
from sqlite3 import Error

# Connect to database
con = sqlite3.connect("products.db")

# Create cursor object
cursorObj = con.cursor()

# # Create table
# cursorObj.execute("""
#     CREATE TABLE employees(
#         id integer PRIMARY KEY,
#         name text,
#         salary real,
#         department text,
#         position text,
#         hireDate text
#     )
# """)

# # Commit chanegs
# con.commit()

# # Insert into table
# entities = (2, 'andrew', 800, 'IT', 'Tech', '2018-02-06')
# cursorObj.execute("""
#     INSERT INTO employees(
#         id,
#         name,
#         salary,
#         department,
#         position,
#         hireDate
#     )
#     VALUES(?,?,?,?,?,?)
# """,
#     entities
# )
# con.commit()

# # Check for table
# cursorObj.execute("""
#     CREATE TABLE IF NOT EXISTS employees(
#         id integer PRIMARY KEY,
#         name text,
#         salary real,
#         department text,
#         position text,
#         hireDate text
#     )
# """)

# # Check for entry
# checkID = 2
# cursorObj.execute("SELECT id FROM employees WHERE id = ?", (checkID,))
# if not cursorObj.fetchall():
#     print("ID 2 does not exist")

# # Catch SQL errors
# try:
#     entities = (2, 'andrew', 800, 'IT', 'Tech', '2018-02-06')
#     cursorObj.execute("""
#         INSERT INTO employees(
#             id,
#             name,
#             salary,
#             department,
#             position,
#             hireDate
#         )
#         VALUES(?,?,?,?,?,?)
#     """,
#         entities
#     )
#     con.commit()
# except sqlite3.Error as error:
#     print(error)

try:
    idToFind = "y"
    cursorObj.execute("""
        SELECT EXISTS(
            SELECT id FROM employees WHERE id=?
        )
    """, idToFind)
    queryResult = cursorObj.fetchall()[0]
    if queryResult == (0,):
        print(None)
    elif queryResult == (1,):
        print('found')
    else:
        print('Unexpected response from database')
except sqlite3.Error as error:
    print(error)



# Close connect with database
con.close()