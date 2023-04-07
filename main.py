import database as db
import scraper as scrape
import time
import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import Ui_MainWindow

# Default variables
cats_to_check = 300
time_between_cats = 1.0
cat_file = "validcategories.txt"
changelog = "changeLog.txt"

# Find which categories are valid
def write_categories(cats_to_check:int, time_between_cats:float):
    # Clear the text file
    clear_file = open(cat_file, 'w')
    clear_file.close()

    with open(cat_file, 'a') as file:
        # Iterate through categories
        for curr_cat in range(cats_to_check):
            win.update_log(f"attempting https://www.prowash.com.au/category/{curr_cat}")
            cat_attempt = scrape.test_category("https://www.prowash.com.au/category/"+str(curr_cat))[0]
            if cat_attempt:
                file.write(f"https://www.prowash.com.au/category/{curr_cat}\n")
                win.update_log("Is valid")
            time.sleep(time_between_cats)

# Counts number of categories category file
def count_categories():
    if os.path.exists(cat_file):
        with open(cat_file, "r") as file:
            final_num = 0
            for category in file.readlines():
                final_num += 1
        return final_num
    else:
        return 0

# Reads and outputs categories in a string format
def read_categories():
    if os.path.exists(cat_file):
        with open(cat_file, "r") as file:
            final_str = ""
            for line in file.readlines():
                final_str += line
        return final_str
    else:
        return "No categories found, please generate."

def read_changelog():
    if not os.path.exists(changelog):
        new_file = open(changelog, 'w')
        new_file.close()
        return ""
    with open(changelog, "r") as file:
        output = ""
        for line in file.readlines():
            output += line
    return output

# updates changelog and outputs in a string format
def prepend_changelog(additions:list, changes:list, sales:list):
    # Put data in right format
    prepend_data = f"##############################\nChanges ({datetime.today().strftime('%Y-%m-%d')})\n##############################\n\nNew products:\n"
    for addition in additions:
        prepend_data += f"\t+ {addition}\n"
    prepend_data += "\nChanged products:\n"
    for change in changes:
        prepend_data += f"\t+ {change}\n"
    prepend_data += "\nNew products on sale:\n"
    for sale in sales:
        prepend_data += f"\t+ {sale}\n"
    # prepend data to changelog
    with open(changelog, "r+") as file:
        content = file.read()
        file.seek(0,0)
        file.write(prepend_data + "\n" + content)

"""
#######################################
Graphics
#######################################
"""

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.UIFunctions()

    # Connecting functions to UI elements
    def UIFunctions(self):
        self.btnBeginSearch.pressed.connect(self.begin_search)
        self.btnBeginScrape.pressed.connect(self.begin_scrape)
        self.btnDelayHint.pressed.connect(self.delay_hint)

    # Begin searching for categories
    def begin_search(self):
        cats_to_check = self.spnMaxCategories.value()
        time_between_cats = self.spnDelay.value()
        write_categories(cats_to_check, time_between_cats)

    # Begin scraping product information
    def begin_scrape(self):
        raise NotImplementedError("to do")
    # Show messagebox explaining delay in scraping
    def delay_hint(self):
        display_messagebox("Delay", "Delay is important in webscraping, since too many requests in quick succession will result in a 429 error.")
    
    # Updating certain text with outputs
    def update_date(self, date:str):
        output = f"Current date: {date}"
        self.lblCurrentDate.setText(output)
    def update_categories_loaded(self, amount:str|int):
        output = f"Categories loaded: {amount}"
        self.lblCategoriesLoaded.setText(output)
    def update_known_products(self, amount:str|int):
        output = f"Known products: {amount}"
        self.lblKnownProducts.setText(output)
    def update_database_status(self, status:str):
        self.lblDatabaseStatus.setText(status)
    def update_changelog(self, text:str):
        self.txtChangelog.setPlainText(text)
    def update_loaded_categories(self, text:str):
        self.txtLoaded.setPlainText(text)
    def update_loaded_status(self, status:str):
        self.lblLoadedStatus.setText(status)
        self.lblCategoriesStatus.setText(status)
    def update_found_categories_list(self, text:str):
        self.txtFound.setPlainText(text)
    def update_found_categories_status(self, status:str):
        self.lblFoundStatus.setText(status)
    def update_log(self, text:str):
        previous_text = self.txtLog.toPlainText()
        current_text = previous_text + text + "\n"
        self.txtLog.setPlainText(current_text)
        print(f"logged: {text}")

    def no_categories(self):
        self.btnBeginScrape.setDisabled(True)
        self.update_categories_loaded("No product categories file loaded")


# Create and display a messagebox
def display_messagebox(title:str, message:str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.exec_()

"""
#######################################
Main
#######################################
"""
# Prepare GUI
app = QApplication(sys.argv)
win = Window()

# Check for categories and database
if not os.path.exists(cat_file) or count_categories() == 0: 
    display_messagebox("Missing category list", "'validCategories.txt' was not found or is empty in the current working directory. No categories have been loaded. Please generate new categories under the 'Product Categories' tab")
    win.no_categories()
else:
    win.update_loaded_status("Product categories are loaded")

if os.stat("products.db").st_size == 0:
    display_messagebox("Missing product database", "'products.db' was not found in the current working directory. A new database will be generated now. Feel free to replace the new database with the old.")
    db.createTables()

# Initialise GUI
win.update_categories_loaded(count_categories())
win.update_found_categories_status("Not currently finding categories.")
win.update_loaded_categories(read_categories())
win.update_known_products(db.query_product_amount())
win.update_date(datetime.today().strftime('%Y-%m-%d'))
win.update_changelog(read_changelog())

if db.query_product_amount() == 0:
    win.update_database_status("Database empty")
else:
    win.update_database_status("Database contains product(s)")
win.update_log("finished initialisation")


win.show()


sys.exit(app.exec())