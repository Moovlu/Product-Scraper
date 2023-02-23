import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_ScraperUI import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.btnGenerateList.pressed.connect(self.printHi)

    def printHi(self):
        print("hi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())