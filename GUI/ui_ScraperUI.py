# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScraperUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(544, 522)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.product_categories = QWidget()
        self.product_categories.setObjectName(u"product_categories")
        self.verticalLayout_4 = QVBoxLayout(self.product_categories)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblProductCategories = QLabel(self.product_categories)
        self.lblProductCategories.setObjectName(u"lblProductCategories")

        self.verticalLayout_4.addWidget(self.lblProductCategories)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblLoadedCategories = QLabel(self.product_categories)
        self.lblLoadedCategories.setObjectName(u"lblLoadedCategories")

        self.verticalLayout_3.addWidget(self.lblLoadedCategories)

        self.txtLoaded = QPlainTextEdit(self.product_categories)
        self.txtLoaded.setObjectName(u"txtLoaded")
        self.txtLoaded.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.txtLoaded)

        self.lblLoadedStatus = QLabel(self.product_categories)
        self.lblLoadedStatus.setObjectName(u"lblLoadedStatus")

        self.verticalLayout_3.addWidget(self.lblLoadedStatus)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblFindCategoriesOnline = QLabel(self.product_categories)
        self.lblFindCategoriesOnline.setObjectName(u"lblFindCategoriesOnline")

        self.verticalLayout_2.addWidget(self.lblFindCategoriesOnline)

        self.txtFound = QPlainTextEdit(self.product_categories)
        self.txtFound.setObjectName(u"txtFound")
        self.txtFound.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.txtFound)

        self.lblFoundStatus = QLabel(self.product_categories)
        self.lblFoundStatus.setObjectName(u"lblFoundStatus")

        self.verticalLayout_2.addWidget(self.lblFoundStatus)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblMaximumText = QLabel(self.product_categories)
        self.lblMaximumText.setObjectName(u"lblMaximumText")

        self.horizontalLayout_2.addWidget(self.lblMaximumText)

        self.spnMaxCategories = QSpinBox(self.product_categories)
        self.spnMaxCategories.setObjectName(u"spnMaxCategories")
        self.spnMaxCategories.setMaximum(999)
        self.spnMaxCategories.setValue(300)

        self.horizontalLayout_2.addWidget(self.spnMaxCategories)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btnBeginSearch = QPushButton(self.product_categories)
        self.btnBeginSearch.setObjectName(u"btnBeginSearch")

        self.verticalLayout_2.addWidget(self.btnBeginSearch)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.product_categories, "")
        self.product_changes = QWidget()
        self.product_changes.setObjectName(u"product_changes")
        self.verticalLayout_8 = QVBoxLayout(self.product_changes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lblProductChanges = QLabel(self.product_changes)
        self.lblProductChanges.setObjectName(u"lblProductChanges")

        self.verticalLayout_8.addWidget(self.lblProductChanges)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lblChangelog = QLabel(self.product_changes)
        self.lblChangelog.setObjectName(u"lblChangelog")

        self.verticalLayout_7.addWidget(self.lblChangelog)

        self.txtChangelog = QPlainTextEdit(self.product_changes)
        self.txtChangelog.setObjectName(u"txtChangelog")
        self.txtChangelog.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.txtChangelog)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lblStatus = QLabel(self.product_changes)
        self.lblStatus.setObjectName(u"lblStatus")

        self.verticalLayout_5.addWidget(self.lblStatus)

        self.lblCategoriesLoaded = QLabel(self.product_changes)
        self.lblCategoriesLoaded.setObjectName(u"lblCategoriesLoaded")

        self.verticalLayout_5.addWidget(self.lblCategoriesLoaded)

        self.lblKnownProducts = QLabel(self.product_changes)
        self.lblKnownProducts.setObjectName(u"lblKnownProducts")

        self.verticalLayout_5.addWidget(self.lblKnownProducts)

        self.lblCurrentDate = QLabel(self.product_changes)
        self.lblCurrentDate.setObjectName(u"lblCurrentDate")

        self.verticalLayout_5.addWidget(self.lblCurrentDate)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.lblDatabaseStatus = QLabel(self.product_changes)
        self.lblDatabaseStatus.setObjectName(u"lblDatabaseStatus")

        self.verticalLayout_6.addWidget(self.lblDatabaseStatus)

        self.lblCategoriesStatus = QLabel(self.product_changes)
        self.lblCategoriesStatus.setObjectName(u"lblCategoriesStatus")

        self.verticalLayout_6.addWidget(self.lblCategoriesStatus)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblDelay = QLabel(self.product_changes)
        self.lblDelay.setObjectName(u"lblDelay")

        self.horizontalLayout_4.addWidget(self.lblDelay)

        self.spnDelay = QDoubleSpinBox(self.product_changes)
        self.spnDelay.setObjectName(u"spnDelay")
        self.spnDelay.setMaximum(5.000000000000000)
        self.spnDelay.setSingleStep(0.100000000000000)
        self.spnDelay.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.spnDelay)

        self.lblSeconds = QLabel(self.product_changes)
        self.lblSeconds.setObjectName(u"lblSeconds")

        self.horizontalLayout_4.addWidget(self.lblSeconds)

        self.btnDelayHint = QPushButton(self.product_changes)
        self.btnDelayHint.setObjectName(u"btnDelayHint")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelayHint.sizePolicy().hasHeightForWidth())
        self.btnDelayHint.setSizePolicy(sizePolicy)
        self.btnDelayHint.setMaximumSize(QSize(23, 23))
        self.btnDelayHint.setCursor(QCursor(Qt.WhatsThisCursor))

        self.horizontalLayout_4.addWidget(self.btnDelayHint)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.btnBeginScrape = QPushButton(self.product_changes)
        self.btnBeginScrape.setObjectName(u"btnBeginScrape")

        self.verticalLayout_5.addWidget(self.btnBeginScrape)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.product_changes, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.txtLog = QPlainTextEdit(self.centralwidget)
        self.txtLog.setObjectName(u"txtLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txtLog.sizePolicy().hasHeightForWidth())
        self.txtLog.setSizePolicy(sizePolicy1)
        self.txtLog.setReadOnly(True)

        self.verticalLayout.addWidget(self.txtLog)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblProductCategories.setText(QCoreApplication.translate("MainWindow", u"Product Categories", None))
        self.lblLoadedCategories.setText(QCoreApplication.translate("MainWindow", u"Loaded Categories", None))
        self.lblLoadedStatus.setText(QCoreApplication.translate("MainWindow", u"Loaded Status Placeholder", None))
        self.lblFindCategoriesOnline.setText(QCoreApplication.translate("MainWindow", u"Find Categories Online", None))
        self.lblFoundStatus.setText(QCoreApplication.translate("MainWindow", u"Found Categories Placeholder", None))
        self.lblMaximumText.setText(QCoreApplication.translate("MainWindow", u"Max category num to check:", None))
        self.btnBeginSearch.setText(QCoreApplication.translate("MainWindow", u"Begin Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.product_categories), QCoreApplication.translate("MainWindow", u"Product Categories", None))
        self.lblProductChanges.setText(QCoreApplication.translate("MainWindow", u"Product Changes", None))
        self.lblChangelog.setText(QCoreApplication.translate("MainWindow", u"Change log", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.lblCategoriesLoaded.setText(QCoreApplication.translate("MainWindow", u"Categories loaded: 0", None))
        self.lblKnownProducts.setText(QCoreApplication.translate("MainWindow", u"Known Products: 0", None))
        self.lblCurrentDate.setText(QCoreApplication.translate("MainWindow", u"Current Date: 0000/00/00", None))
        self.lblDatabaseStatus.setText(QCoreApplication.translate("MainWindow", u"Placeholder database status", None))
        self.lblCategoriesStatus.setText(QCoreApplication.translate("MainWindow", u"Placeholder categories status", None))
        self.lblDelay.setText(QCoreApplication.translate("MainWindow", u"Delay:", None))
        self.lblSeconds.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.btnDelayHint.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.btnBeginScrape.setText(QCoreApplication.translate("MainWindow", u"Begin scraping products", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.product_changes), QCoreApplication.translate("MainWindow", u"Product Changes", None))
    # retranslateUi

