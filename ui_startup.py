# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startupsNHfce.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Startup(object):
    def setupUi(self, Startup):
        if not Startup.objectName():
            Startup.setObjectName(u"Startup")
        Startup.resize(400, 200)
        Startup.setMinimumSize(QSize(400, 200))
        Startup.setMaximumSize(QSize(400, 200))
        font = QFont()
        font.setFamily(u"Poppins")
        Startup.setFont(font)
        icon = QIcon()
        icon.addFile(u"assets/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Startup.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Startup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Startup)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Poppins Medium")
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Startup)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Poppins Medium")
        font2.setPointSize(9)
        self.label_2.setFont(font2)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(Startup)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(56, 56))
        self.pushButton_2.setMaximumSize(QSize(56, 56))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius: 28px;\n"
"border: 2px solid black;")
        icon1 = QIcon()
        icon1.addFile(u"assets/default.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(54, 54))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(9)
        self.label_3.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setFamily(u"Poppins Medium")
        self.pushButton.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Startup)

        QMetaObject.connectSlotsByName(Startup)
    # setupUi

    def retranslateUi(self, Startup):
        Startup.setWindowTitle(QCoreApplication.translate("Startup", u"Details Calculator SDRF", None))
        self.label.setText(QCoreApplication.translate("Startup", u"Details Calculator SDRF", None))
        self.label_2.setText(QCoreApplication.translate("Startup", u"Details Calculator SDRF, is a specialized tool designed to facilitate real estate calculations, particularly focusing on property cost assessments.", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Startup", u"Choose Image", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Startup", u"Hi, who will be using this app?", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Startup", u"Your Name", None))
        self.pushButton.setText(QCoreApplication.translate("Startup", u"Next", None))
    # retranslateUi

