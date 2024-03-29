import requests
from bs4 import BeautifulSoup
import database as db
from datetime import datetime


# Test if current site is valid
def test_category(URL:str):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    try:
        panel = soup.find_all("div", id="pnlTopic")
        error_text = panel[0].find("div", class_="col-md-12").text
        return False, error_text.strip()
    except:
        return True, None

# Check for multiple pages
def multiple_page_check(soup:str):
    pages = []
    page_selection = soup.find_all("ul", class_="pagination")
    if page_selection != []:
        page_numbers = page_selection[0].find_all("a", class_="page-number")
        # Append found pages to array
        for entry in page_numbers:
            pages.append(f"https://www.prowash.com.au{entry['href']}")
    return pages
    
# Grab products from category
def add_products(URL:str, database):
    additions = {}
    before_changes = {}
    changes = {}
    before_sales = {}
    sales = {}

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Check for multiple pages
    pages = multiple_page_check(soup)
    pages_parsed = 1

    while True:
        # Find all products on page
        products = soup.find_all("div", class_="entity-page-product")

        for item in products:
        # Stock, Product code, Product name, Regular price, Sale price
            item_details = [None, None, None, None, None]

            # Identify if product is available in store
            try:
                if item.find("div", class_="entity-product-stock-wrap"):               
                    # Find stock status
                    if item.find("div", class_="stock-hint").text.strip() == "In Stock":
                        item_details[0] = 1
                    else:
                        item_details[0] = 0
                    # Find product code
                    item_details[1] = item.find("div", class_="entity-product-stock-wrap").text.strip().lstrip("Out of Stock").lstrip("In Stock\r\nCode:").strip()
                    # Find product name
                    item_details[2] = item.find("div", class_="entity-product-name-wrap").text
                    # Check if item is on sale
                    if item.find("div", class_="oldprice"):
                        # Find product regular price
                        item_details[3] = float(item.find("div", class_="oldprice").text.strip("Regular Price: $").replace(",",""))
                        # Find product sale price
                        item_details[4] = float(item.find("div", class_="sale-price").text.strip("Clearance Price: $").strip("On Sale For: $").strip("Price: $").replace(",",""))
                    else:
                        # Find product regular price
                        item_details[3] = float(item.find("div", class_="entity-product-price-wrap").text.strip("Price: $").replace(",",""))
                        # There is no sale price for this product
                        item_details[4] = None

                # Check if product is online order only
                elif item.find("div", class_="call-to-order-wrap"):
                    # No stock status
                    item_details[0] = None
                    # Find product code
                    item_details[1] = item.text.split("\n")[3].lstrip(" Code:").rstrip("\r")
                    # Find product name
                    item_details[2] = item.find("div", class_="entity-product-name-wrap").text.strip()
                    # No regular price
                    item_details[3] = None
                    # No sale price
                    item_details[4] = None
                else:
                    print("Unidentified product on", URL)
            except ValueError:
                print(f"Product does not conform to common format: {item}")

            if item_details[1] is None:
                print("Skipping...")
            # Check if product exists in database
            elif database.queryProductExistance(item_details[1]) is False:
                # Write to additions dictionary
                additions[item_details[1]] = [item_details[0], item_details[2], item_details[3], item_details[4]]
                # Write product to database
                database.insertData(item_details[1],item_details[2],item_details[0])
                print("Added item", item_details[1])
                # Write product price to database
                database.insertPrices(datetime.today(), item_details[1], item_details[3], item_details[4])
                print("Added price", item_details[1])
            else:
                # Make sure the product's price isn't a duplicate to the most recent entry
                if database.queryCurrentSalePrice(item_details[1]) != item_details[4]:
                    before_sales[item_details[1]] = database.queryCurrentSalePrice(item_details[1])
                    sales[item_details[1]] = item_details[4]
                    database.insertPrices(datetime.today(), item_details[1], item_details[3], item_details[4])
                    print("Adjusted sale price", item_details[1])

                if database.queryCurrentPrice(item_details[1]) != item_details[3]:
                    before_changes[item_details[1]] = database.queryCurrentPrice(item_details[1])
                    changes[item_details[1]] = item_details[3]
                    database.insertPrices(datetime.today(), item_details[1], item_details[3], item_details[4])
                    print("Adjusted price", item_details[1])


        # Check if all pages have been parsed
        if (pages_parsed >= len(pages)):
            break
        else:
            # Parse next page
            page = requests.get(pages[pages_parsed])
            soup = BeautifulSoup(page.content, "html.parser")
            pages_parsed += 1
    return additions, before_changes, changes, before_sales, sales


# Test Case
if __name__ == "__main__":
    data = db.Database()
    URL = "https://www.prowash.com.au/category/235"

    print("Testing categories")
    test_category(URL) # Makes sure URL category is valid, returns (T/F, Errormsg)

    print("Appending category to database")
    add_products("https://www.prowash.com.au/category/235", data) # Appends products found on page to database