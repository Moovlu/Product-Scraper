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
            CREATE TABLE IF NOT EXISTS MainData(
                productCode text PRIMARY KEY,
                name text NOT NULL,
                inStock integer
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prices(
                date datetime PRIMARY KEY,
                productCode text,
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

# Query database for existance of product id
def queryProductExistance(productCode:str):
    try:
        cursor.execute("""
            SELECT EXISTS(
                SELECT productCode FROM MainData WHERE productCode = ?
            )
        """, [productCode])

        queryResult = cursor.fetchall()[0]
        if queryResult == (0,):
            return False
        elif queryResult == (1,):
            return True
        else:
            print('Unexpected response from database')
            return False

    except sqlite3.Error as error:
        print(error)

# Query database for most recent price of given product number
def queryCurrentPrice(productCode:str):
    try:
        cursor.execute("""
            SELECT *
            FROM Prices
            WHERE productCode = ?
            ORDER BY date DESC
        """, [productCode])

        queryResult = cursor.fetchall()
        queryFiltered = [x[2] for x in queryResult][0]
        return (queryFiltered)

    except sqlite3.Error as error:
        print(error)

# Query 
def queryCurrentSalePrice(productCode:str):
    try:
        cursor.execute("""
            SELECT *
            FROM Prices
            WHERE productCode = ?
            ORDER BY date DESC
        """, [productCode])

        queryResult = cursor.fetchall()
        queryFiltered = [x[3] for x in queryResult][0]
        return (queryFiltered)

    except sqlite3.Error as error:
        print(error)

# Close database
def close():
    con.close()