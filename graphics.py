import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


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
        raise NotImplementedError("to do")
    # Begin scraping product information
    def begin_scrape(self):
        raise NotImplementedError("to do")
    # Show messagebox explaining delay in scraping
    def delay_hint(self):
        raise NotImplementedError("to do")
    
    def update_date(self, date:str):
        self.lblCurrentDate.setText(date)
    def update_categories_loaded(self):
        pass
    def update_known_products(self):
        pass
    def update_database_status(self):
        pass
    def update_categories_status(self):
        pass
    def update_changelog(self):
        pass
    def update_loaded_categories(self):
        pass
    def update_loaded_status(self):
        pass
    def update_found_categories(self):
        pass
    def update_found_categories_count(self):
        pass
    def update_log(self):
        pass

# Test Case
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())