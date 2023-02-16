# Import modules
import database as db
import scraper as scrape
import time

# Default variables
categoriesToCheck = 300
TimeDelayBetweenCategories = 1

# Find which categories are valid
def checkCategories():
    # Clear the text file
    clearFile = open('validcategories.txt', 'w')
    clearFile.close()

    with open('validcategories.txt', 'a') as file:
        # Iterate through categories
        for currentCategory in range(categoriesToCheck):
            print("attempting","https://www.prowash.com.au/category/"+str(currentCategory))
            if scrape.TestUrl("https://www.prowash.com.au/category/"+str(currentCategory))[0] == True:
                file.write("https://www.prowash.com.au/category/"+str(currentCategory)+"\n")
                print("Found!")
            time.sleep(TimeDelayBetweenCategories)

db.createTables()
checkCategories()

# scrape.AddProducts("https://www.prowash.com.au/category/233/security")

# print(db.queryCurrentSalePrice('DH29141'))

# Find valid categories, write to file

# db.close()