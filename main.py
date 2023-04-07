import database as db
import scraper as scrape
import time
import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5 import QtTest
from gui import Ui_MainWindow

# Default variables
cats_to_check = 300
time_between_cats = 1.0
cat_file = "validcategories.txt"
changelog = "changeLog.txt"

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
def prepend_changelog(additions:dict, before_changes:dict, after_changes:dict, before_sales:dict, after_sales:dict):
    # Put data in right format
    prepend_data = f"##############################\nChanges ({datetime.today().strftime('%Y-%m-%d')})\n##############################\n\nNew products:\n"
    for addition in additions:
        prepend_data += f"\t+ {addition} - {additions[addition]}\n"
    prepend_data += "\nRegular price changes:\n"
    for change in before_changes:
        prepend_data += f"\t+ {change} - {before_changes[change]} -> {after_changes[change]}\n"
    prepend_data += "\nSale price changes:\n"
    for sale in before_sales:
        prepend_data += f"\t+ {sale} - {before_sales[sale]} -> {after_sales[sale]}\n"
    # prepend data to changelog
    with open(changelog, "r+") as file:
        content = file.read()
        file.seek(0,0)
        file.write(prepend_data + "\n" + content)

"""
#######################################
Threaded tasks
#######################################
"""

class CategoryWorker(QObject):
    finished = pyqtSignal()
    current_url = pyqtSignal(str)
    valid_url = pyqtSignal(str)

    def run(self):
        cats_to_check = win.spnMaxCategories.value()
        time_between_cats = win.spnDelay.value()
        # Clear the text file
        clear_file = open(cat_file, 'w')
        clear_file.close()
        
        with open(cat_file, 'a') as file:
        # Iterate through categories
            for curr_cat in range(cats_to_check):
                self.current_url.emit(f"Attempting https://www.prowash.com.au/category/{curr_cat}")
                cat_attempt = scrape.test_category("https://www.prowash.com.au/category/"+str(curr_cat))[0]
                if cat_attempt:
                    file.write(f"https://www.prowash.com.au/category/{curr_cat}\n")
                    self.valid_url.emit(f"https://www.prowash.com.au/category/{curr_cat}")
                time.sleep(time_between_cats)
        self.finished.emit()


class ScrapingWorker(QObject):
    finished = pyqtSignal()
    current_url = pyqtSignal(str)

    def run(self):
        additions = {}
        before_changes = {}
        after_changes = {}
        before_sales = {}
        after_sales = {}

        with open(cat_file, 'r') as file:
            # Iterate through file
            for line in file.readlines():
                self.current_url.emit(f"Parsing {line.strip()}")
                # Update database and append item changes and additions to dicts
                t_additions, t_before_changes, t_after_changes, t_before_sales, t_after_sales = scrape.add_products(line.strip())
                additions.update(t_additions)
                before_changes.update(t_before_changes)
                after_changes.update(t_after_changes)
                before_sales.update(t_before_sales)
                after_sales.update(t_after_sales)
        # Write changes and additions to log
        prepend_changelog(additions, before_changes, after_changes, before_sales, after_sales)
        self.finished.emit()
        


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
        self.clear_categories_list()
        
        self.thread = QThread(parent=self)
        self.worker = CategoryWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        
        self.worker.current_url.connect(self.update_found_categories_status)
        self.worker.valid_url.connect(self.cat_valid_url)

        self.thread.start()

        self.btnBeginSearch.setDisabled(True)
        self.btnBeginScrape.setDisabled(True)
        self.thread.finished.connect(self.finished_categories)

    def cat_valid_url(self, text):
        self.update_log(text)
        self.update_found_categories_list(text)

    def finished_categories(self):
        self.btnBeginSearch.setEnabled(True)
        self.update_found_categories_status("Not currently finding categories.")
        self.update_categories_loaded(count_categories())
        self.update_loaded_categories(read_categories())
        if count_categories() > 0:
            self.update_loaded_status("Product categories are loaded")
            self.btnBeginScrape.setEnabled(True)

    # Begin scraping product information
    def begin_scrape(self):
        self.thread = QThread(parent=self)
        self.worker = ScrapingWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        
        self.worker.current_url.connect(self.log_current_category)

        self.thread.start()

        self.btnBeginSearch.setDisabled(True)
        self.btnBeginScrape.setDisabled(True)
        self.thread.finished.connect(self.finished_scrape)

    def log_current_category(self, text):
        self.update_log(text)
    
    def finished_scrape(self):
        self.btnBeginSearch.setEnabled(True)
        self.btnBeginScrape.setEnabled(True)
        self.update_changelog(read_changelog())
        self.update_known_products(db.query_product_amount())

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
    def update_found_categories_status(self, status:str):
        self.lblFoundStatus.setText(status)
        self.update_log(status)
    def clear_categories_list(self):
        self.txtLoaded.setPlainText("")
        self.txtFound.setPlainText("")
    def update_found_categories_list(self, text:str):
        previous_text = self.txtFound.toPlainText()
        current_text = previous_text + text + "\n"
        self.txtFound.setPlainText(current_text)
    def update_log(self, text:str):
        previous_text = self.txtLog.toPlainText()
        current_text = previous_text + text + "\n"
        self.txtLog.setPlainText(current_text)
        print(f"logged: {text}")

    def no_categories(self):
        self.btnBeginScrape.setDisabled(True)
        self.update_categories_loaded(0)
        self.update_loaded_status("No product categories file loaded")


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
win.update_loaded_categories(read_categories())
win.update_found_categories_status("Not currently finding categories.")
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