# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutPeCeFl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(400, 340)
        About.setMinimumSize(QSize(400, 340))
        About.setMaximumSize(QSize(400, 340))
        icon = QIcon()
        icon.addFile(u"assets/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        About.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(About)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u"assets/icon.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Poppins Medium")
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.label_4 = QLabel(About)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Poppins Medium")
        font1.setPointSize(9)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"padding-top:10px;")
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.label_8 = QLabel(About)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"padding-left:1px;")

        self.verticalLayout.addWidget(self.label_8)

        self.label_3 = QLabel(About)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"padding-top:8px;")

        self.verticalLayout.addWidget(self.label_3)

        self.frame_3 = QFrame(About)
        self.frame_3.setObjectName(u"frame_3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 20px;")
        self.label_7.setPixmap(QPixmap(u"assets/dev-icn.webp"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font1)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font1)
        self.label_6.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_6)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About - Details Calculator SDRF", None))
        self.label_2.setText(QCoreApplication.translate("About", u"Details Calculator SDRF", None))
        self.label_4.setText(QCoreApplication.translate("About", u"Details Calculator SDRF is a desktop application designed to calculate and manage detailed property and financial information related to real estate transactions. It provides a user-friendly interface for inputting and calculating various parameters such as the land area, built-up area, government values, stamp duty, and registration fees.", None))
        self.label_8.setText(QCoreApplication.translate("About", u"Version: ---", None))
        self.label_3.setText(QCoreApplication.translate("About", u"Designed & Developed by:", None))
        self.label_5.setText(QCoreApplication.translate("About", u"Pratham Raj Singh", None))
        self.label_6.setText(QCoreApplication.translate("About", u"Visit: <a href=\"https://imprs.vercel.app/\">imprs.vercel.app</a>", None))
    # retranslateUi

