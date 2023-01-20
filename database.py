# Import modules
import sqlite3
from sqlite3 import Error

# Connect to database
con = sqlite3.connect("products.db")
cursor = con.cursor()

# Fill database with tables
def createTables():
    try:
        cursor.execute("""
            CREATE TABLE MainData(
                productCode varchar(7) PRIMARY KEY,
                name text NOT NULL,
                inStock integer NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE Prices(
                date datetime PRIMARY KEY,
                productCode varchar(7),
                regPrice float,
                salePrice float,
                FOREIGN KEY (productCode)
                    REFERENCES MainData (productCode)
            );
        """)
        con.commit()
    except sqlite3.Error as error:
        print(error)

# Insert product entry into table
def insertData(productCode:str, name:str, inStock:int):
    try:
        cursor.execute("""
            INSERT INTO MainData (productCode, name, inStock)
            VALUES (?,?,?)
        """,
            (productCode, name, inStock)
        )
        con.commit()
    except sqlite3.Error as error:
        print(error)

# Insert price entry into table
def insertPrices(date:str, productCode:str, regPrice:float, salePrice:float):
    try:
        cursor.execute("""
            INSERT INTO Prices (date, productCode, regPrice, salePrice)
            VALUES (?,?,?,?)
        """,
            (date, productCode, regPrice, salePrice)
        )
        con.commit()
    except sqlite3.Error as error:
        print(error)

# Close database
def close():
    con.close()