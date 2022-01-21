# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'test.ui'
##
# Created by: Qt User Interface Compiler version 6.2.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLayout, QMainWindow, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QVBoxLayout, QWidget)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 551)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainContainerVLayout = QVBoxLayout()
        self.mainContainerVLayout.setObjectName(u"mainContainerVLayout")
        self.mainContainerVLayout.setSizeConstraint(
            QLayout.SetDefaultConstraint)
        self.titleLbl = QLabel(self.centralwidget)
        self.titleLbl.setObjectName(u"titleLbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.titleLbl.sizePolicy().hasHeightForWidth())
        self.titleLbl.setSizePolicy(sizePolicy)
        self.titleLbl.setBaseSize(QSize(0, 200))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.titleLbl.setFont(font)
        self.titleLbl.setLayoutDirection(Qt.RightToLeft)
        self.titleLbl.setStyleSheet(u"background: #28dada;\n"
                                    "padding: 1px 20px;")
        self.titleLbl.setLineWidth(1)
        self.titleLbl.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.mainContainerVLayout.addWidget(self.titleLbl)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resultLbl = QLabel(self.frame)
        self.resultLbl.setObjectName(u"resultLbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.resultLbl.sizePolicy().hasHeightForWidth())
        self.resultLbl.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(29)
        font1.setBold(True)
        self.resultLbl.setFont(font1)
        self.resultLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.resultLbl)

        self.descriptionLbl = QLabel(self.frame)
        self.descriptionLbl.setObjectName(u"descriptionLbl")
        self.descriptionLbl.setAlignment(Qt.AlignCenter)
        self.descriptionLbl.setMaximumWidth(600)
        self.descriptionLbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.descriptionLbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.suraLbl = QLabel(self.frame)
        self.suraLbl.setObjectName(u"suraLbl")
        self.suraLbl.setAlignment(
            Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.suraLbl)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ayeTextLbl = QLabel(self.frame)
        self.ayeTextLbl.setMaximumWidth(600)
        self.ayeTextLbl.setWordWrap(True)
        self.ayeTextLbl.setObjectName(u"ayeTextLbl")
        self.ayeTextLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ayeTextLbl)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.mainContainerVLayout.addWidget(self.frame)

        self.newBtn = QPushButton(self.centralwidget)
        self.newBtn.setObjectName(u"newBtn")
        self.newBtn.setMinimumSize(QSize(0, 75))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        self.newBtn.setFont(font2)

        self.mainContainerVLayout.addWidget(self.newBtn)

        self.gridLayout.addLayout(self.mainContainerVLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 364, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Estexare - \u0627\u0633\u062a\u062e\u0627\u0631\u0647", None))
        self.actionNew.setText(
            QCoreApplication.translate("MainWindow", u"New", None))
        self.action.setText(
            QCoreApplication.translate("MainWindow", u"-", None))
        self.actionQuit.setText(
            QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", u"About", None))
        self.titleLbl.setText(QCoreApplication.translate(
            "MainWindow", u"استخاره", None))
        self.resultLbl.setText(QCoreApplication.translate(
            "MainWindow", u"روی استخاره جدید کلیک کنید", None))
        self.descriptionLbl.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.suraLbl.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.ayeTextLbl.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.newBtn.setText(QCoreApplication.translate(
            "MainWindow", u"استخاره جدید", None))
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
