# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(589, 565)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(110, 110))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_logo = QLabel(self.frame_4)
        self.l_logo.setObjectName(u"l_logo")
        self.l_logo.setMinimumSize(QSize(100, 100))
        self.l_logo.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_3.addWidget(self.l_logo)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Miriam Libre"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"background-color: rgba(0,0,0,120);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgba(0,0,0,140);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.te_words = QTextEdit(self.frame_6)
        self.te_words.setObjectName(u"te_words")
        self.te_words.setMaximumSize(QSize(400, 16777215))
        self.te_words.setStyleSheet(u"background-color: rgba(255,255,255,200);")
        self.te_words.setFrameShape(QFrame.NoFrame)
        self.te_words.setFrameShadow(QFrame.Plain)
        self.te_words.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.te_words.setOverwriteMode(True)

        self.horizontalLayout_5.addWidget(self.te_words)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"#frame_3 {\n"
"background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(200, -1, 200, -1)
        self.bt_dir = QPushButton(self.frame_3)
        self.bt_dir.setObjectName(u"bt_dir")
        self.bt_dir.setMaximumSize(QSize(80, 80))
        self.bt_dir.setIconSize(QSize(64, 64))

        self.horizontalLayout_4.addWidget(self.bt_dir)

        self.bt_start = QPushButton(self.frame_3)
        self.bt_start.setObjectName(u"bt_start")
        self.bt_start.setMaximumSize(QSize(80, 80))
        self.bt_start.setIconSize(QSize(64, 64))

        self.horizontalLayout_4.addWidget(self.bt_start)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Image Scraper", None))
        self.bt_dir.setText("")
        self.bt_start.setText("")
    # retranslateUi

