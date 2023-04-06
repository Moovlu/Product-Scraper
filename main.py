import database as db
import scraper as scrape
import graphics as gui
import time
import sys
from PyQt5.QtWidgets import QApplication

# Default variables
cats_to_check = 300
time_between_cats = 1.0
cat_file = "validcategories.txt"

# Find which categories are valid
def checkCategories():
    # Clear the text file
    clear_file = open(cat_file, 'w')
    clear_file.close()

    with open(cat_file, 'a') as file:
        # Iterate through categories
        for curr_cat in range(cats_to_check):
            print(f"attempting https://www.prowash.com.au/category/{curr_cat}")
            cat_attempt = scrape.TestCategory("https://www.prowash.com.au/category/"+str(curr_cat))[0]
            if cat_attempt:
                file.write(f"https://www.prowash.com.au/category/{curr_cat}\n")
                print("Found!")
            time.sleep(time_between_cats)


"""
#######################################
Main section
#######################################
"""

# Start UI
app = QApplication(sys.argv)
win = gui.Window()
win.show()

win.update_date("what a cool date")


sys.exit(app.exec())