# Import modules
import sqlite3
from sqlite3 import Error
import datetime


class Database():
    # Connect to database
    def __init__(self):
        self.con = sqlite3.connect("products.db")
        self.cursor = self.con.cursor()

    # Fill database with tables
    def createTables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS MainData(
                    productCode text PRIMARY KEY,
                    name text NOT NULL,
                    inStock integer
                );
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Prices(
                    date datetime PRIMARY KEY,
                    productCode text,
                    regPrice float,
                    salePrice float,
                    FOREIGN KEY (productCode)
                        REFERENCES MainData (productCode)
                );
            """)
            self.con.commit()
        except sqlite3.Error as error:
            print(error)

    # Insert product entry into table
    def insertData(self, product_code:str, name:str, in_stock:int):
        try:
            self.cursor.execute("""
                INSERT INTO MainData (productCode, name, inStock)
                VALUES (?,?,?)
            """,
                (product_code, name, in_stock)
            )
            self.con.commit()
        except sqlite3.Error as error:
            print(error)

    # Insert price entry into table
    def insertPrices(self, date:str, product_code:str, reg_price:float, sale_price:float):
        try:
            self.cursor.execute("""
                INSERT INTO Prices (date, productCode, regPrice, salePrice)
                VALUES (?,?,?,?)
            """,
                (date, product_code, reg_price, sale_price)
            )
            self.con.commit()
        except sqlite3.Error as error:
            print(error)

    # Query database for existance of product id
    def queryProductExistance(self, product_code:str):
        try:
            self.cursor.execute("""
                SELECT EXISTS(
                    SELECT productCode FROM MainData WHERE productCode = ?
                )
            """, [product_code])

            query_result = self.cursor.fetchall()[0]
            if query_result == (0,):
                return False
            elif query_result == (1,):
                return True
            else:
                print('Unexpected response from database')
                return False

        except sqlite3.Error as error:
            print(error)

    # Query database for most recent price of given product number
    def queryCurrentPrice(self, product_code:str):
        try:
            self.cursor.execute("""
                SELECT *
                FROM Prices
                WHERE productCode = ?
                ORDER BY date DESC
            """, [product_code])

            query_result = self.cursor.fetchall()
            query_filtered = [x[2] for x in query_result][0]
            return (query_filtered)

        except sqlite3.Error as error:
            print(error)

    # Query database for sale price
    def queryCurrentSalePrice(self, product_code:str):
        try:
            self.cursor.execute("""
                SELECT *
                FROM Prices
                WHERE productCode = ?
                ORDER BY date DESC
            """, [product_code])

            query_result = self.cursor.fetchall()
            query_filtered = [x[3] for x in query_result][0]
            return (query_filtered)

        except sqlite3.Error as error:
            print(error)

    # Query amount of products in database
    def query_product_amount(self):
        try:
            self.cursor.execute("""
                SELECT COUNT(*)
                FROM MainData""")

            query_result = self.cursor.fetchall()
            query_filtered = query_result[0][0]
            return query_filtered
        except sqlite3.Error as error:
            print(error)

    # Close database
    def close(self):
        self.con.close()


# Test Case
if __name__ == '__main__':
    # Test variables
    product_code = "test_productcode"
    product_name = "test-product"
    in_stock = 1
    product_price = 10
    sale_price = 0
    db = Database()

    print("Creating tables")
    db.createTables() # Create a new table

    print("Inserting data")
    db.insertData(product_code, product_name, in_stock) # Create a new product

    print("Inserting prices")
    db.insertPrices(datetime.datetime.today(), product_code, product_price, sale_price) # Add price to product

    print("Checking existance")
    print(f'Existance: {db.queryProductExistance(product_code)}') # Check product existance

    print("Check current price")
    print(f"Current price: {db.queryCurrentPrice(product_code)}") # Get current product price

    print("Get sale price")
    print(f"Sale price: {db.queryCurrentSalePrice(product_code)}") # Get current sale price

    print("Count database items")
    print(f"Number of items: {db.query_product_amount()}")
    
    db.close() # Close database