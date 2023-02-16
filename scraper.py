# Import modules
import requests
from bs4 import BeautifulSoup
import database as db
from datetime import datetime

# Test variables
URL = "https://www.prowash.com.au/category/235"

# Test if current site is valid
def TestUrl(URL:str):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    try:
        panel = soup.find_all("div", id="pnlTopic")
        errorText = panel[0].find("div", class_="col-md-12").text
        return False, errorText.strip()
    except:
        return True, None

# Grab products from category
def AddProducts(URL:str):
    pages = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Check for multiple pages
    pageSelection = soup.find_all("ul", class_="pagination")
    if pageSelection != []:
        pageNumbers = pageSelection[0].find_all("a", class_="page-number")
        # Append found pages to array
        for entry in pageNumbers:
            pages.append("https://www.prowash.com.au"+entry["href"])

    pagesParsed = 1
    while True:
        
        # Find all products on page
        products = soup.find_all("div", class_="entity-page-product")

        for item in products:
        # Stock, Product code, Product name, Regular price, Sale price
            itemDetails = [None, None, None, None, None]

        #Identify if product is available in store
            if item.find("div", class_="entity-product-stock-wrap"):               
                # Find stock status
                if item.find("div", class_="stock-hint").text.strip() == "In Stock":
                    itemDetails[0] = 1
                else:
                    itemDetails[0] = 0
                # Find product code
                itemDetails[1] = item.find("div", class_="entity-product-stock-wrap").text.strip().lstrip("Out of Stock").lstrip("In Stock\r\nCode:").strip()
                # Find product name
                itemDetails[2] = item.find("div", class_="entity-product-name-wrap").text
                # Check if item is on sale
                if item.find("div", class_="oldprice"):
                    # Find product regular price
                    itemDetails[3] = float(item.find("div", class_="oldprice").text.strip("Regular Price: $"))
                    # Find product sale price
                    itemDetails[4] = float(item.find("div", class_="sale-price").text.strip("Clearance Price: $"))
                else:
                    # Find product regular price
                    itemDetails[3] = float(item.find("div", class_="entity-product-price-wrap").text.strip("Price: $"))
                    # There is no sale price for this product
                    itemDetails[4] = None

        #Check if product is online order only
            elif item.find("div", class_="call-to-order-wrap"):
                # No stock status
                itemDetails[0] = None
                # Find product code
                itemDetails[1] = item.text.split("\n")[3].lstrip(" Code:").rstrip("\r")
                # Find product name
                itemDetails[2] = item.find("div", class_="entity-product-name-wrap").text.strip()
                # No regular price
                itemDetails[3] = None
                # No sale price
                itemDetails[4] = None
            else:
                print("Unidentified product on", URL)

            # Check if product exists in database
            if db.queryProductExistance(itemDetails[1]) == False:
                # Write product to database
                db.insertData(itemDetails[1],itemDetails[2],itemDetails[0])
                print("Added item", itemDetails[1])
                # Write product price to database
                db.insertPrices(datetime.today(), itemDetails[1], itemDetails[3], itemDetails[4])
                print("Added price", itemDetails[1])
            else:
                # Make sure the product's price isn't a duplicate to the most recent entry
                if db.queryCurrentSalePrice(itemDetails[1]) != itemDetails[4]:
                    db.insertPrices(datetime.today(), itemDetails[1], itemDetails[3], itemDetails[4])
                    print("Adjusted sale price", itemDetails[1])
                if db.queryCurrentPrice(itemDetails[1]) != itemDetails[3]:
                    db.insertPrices(datetime.today(), itemDetails[1], itemDetails[3], itemDetails[4])
                    print("Adjusted price", itemDetails[1])

        # Check if all pages have been parsed
        if (pagesParsed >= len(pages)):
            break
        else:
            # Parse next page
            page = requests.get(pages[pagesParsed])
            soup = BeautifulSoup(page.content, "html.parser")
            pagesParsed += 1