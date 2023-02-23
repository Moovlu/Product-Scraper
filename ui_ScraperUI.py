from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 299)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(38, 41, 52);\n"
"border: 2px solid #212121;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(30)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"border: none;\n"
"color: rgb(158, 158, 158);")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnGenerateList = QPushButton(self.frame)
        self.btnGenerateList.setObjectName(u"btnGenerateList")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenerateList.sizePolicy().hasHeightForWidth())
        self.btnGenerateList.setSizePolicy(sizePolicy)
        self.btnGenerateList.setMinimumSize(QSize(130, 25))
        self.btnGenerateList.setBaseSize(QSize(130, 25))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.btnGenerateList.setFont(font3)
        self.btnGenerateList.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #32aa9c;\n"
"    border-radius: 6px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(44, 189, 146, 255), stop:1 rgba(55, 204, 166, 255));\n"
"    min-width: 80px;\n"
"	color: rgb(15, 15, 15);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(64, 209, 166, 255), stop:1 rgba(75, 224, 186, 255));\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid #a0dda5\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnGenerateList)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btnLocateFile = QPushButton(self.frame)
        self.btnLocateFile.setObjectName(u"btnLocateFile")
        sizePolicy.setHeightForWidth(self.btnLocateFile.sizePolicy().hasHeightForWidth())
        self.btnLocateFile.setSizePolicy(sizePolicy)
        self.btnLocateFile.setMinimumSize(QSize(130, 25))
        self.btnLocateFile.setBaseSize(QSize(130, 25))
        self.btnLocateFile.setFont(font3)
        self.btnLocateFile.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #212121;\n"
"    border-radius: 6px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(38, 41, 52, 255), stop:1 rgba(52, 56, 72, 255));\n"
"    min-width: 80px;\n"
"	color: rgb(243, 245, 245);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(58, 61, 72, 255), stop:1 rgba(72, 76, 82, 255));\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid #2cbd92\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnLocateFile)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pbListOutput = QProgressBar(self.frame)
        self.pbListOutput.setObjectName(u"pbListOutput")
        self.pbListOutput.setFont(font3)
        self.pbListOutput.setValue(0)
        self.pbListOutput.setTextVisible(False)

        self.verticalLayout.addWidget(self.pbListOutput)

        self.lblListOutput = QLabel(self.frame)
        self.lblListOutput.setObjectName(u"lblListOutput")
        self.lblListOutput.setFont(font3)
        self.lblListOutput.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.lblListOutput)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Could not find valid categories", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"You can either generate a new list or find the file manually", None))
        self.btnGenerateList.setText(QCoreApplication.translate("MainWindow", u"Generate a new list", None))
        self.btnLocateFile.setText(QCoreApplication.translate("MainWindow", u"Locate file", None))
        self.lblListOutput.setText(QCoreApplication.translate("MainWindow", u"File missing", None))
    # retranslateUi

