# Import modules
import requests
from bs4 import BeautifulSoup

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
def ReadProducts(URL:str):
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
        
        products = soup.find_all("div", class_="entity-page-product")
        #TODO: Put try loop here
        for item in products:
            # Check if product is in stock or not
            if item.find("entity-product-stock-wrap"):
                print("found it")



        # Check if all pages have been parsed
        if (pagesParsed > len(pages)):
            break
        else:
            # Parse next page
            page = requests.get(pages[pagesParsed])
            soup = BeautifulSoup(page.content, "html.parser")
            pagesParsed += 1

        # Product code, name, status, regular price, sale price



ReadProducts("https://www.prowash.com.au/category/233/security")