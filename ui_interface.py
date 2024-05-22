# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceqjnVZt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Interface(object):
    def setupUi(self, Interface):
        if not Interface.objectName():
            Interface.setObjectName(u"Interface")
        Interface.resize(1000, 600)
        Interface.setMinimumSize(QSize(1000, 600))
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(9)
        Interface.setFont(font)
        self.CW = QWidget(Interface)
        self.CW.setObjectName(u"CW")
        self.verticalLayout = QVBoxLayout(self.CW)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.app_header = QFrame(self.CW)
        self.app_header.setObjectName(u"app_header")
        self.app_header.setFrameShape(QFrame.StyledPanel)
        self.app_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.app_header)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 7)
        self.app_name = QLabel(self.app_header)
        self.app_name.setObjectName(u"app_name")
        font1 = QFont()
        font1.setFamily(u"Poppins Medium")
        font1.setPointSize(12)
        self.app_name.setFont(font1)

        self.verticalLayout_2.addWidget(self.app_name)

        self.frame_10 = QFrame(self.app_header)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(0, 20))
        self.frame_10.setMaximumSize(QSize(16777215, 20))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;")
        icon = QIcon()
        icon.addFile(u"assets/default.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.username_title = QLabel(self.frame_10)
        self.username_title.setObjectName(u"username_title")
        self.username_title.setMaximumSize(QSize(16777215, 20))
        self.username_title.setFont(font)

        self.horizontalLayout_6.addWidget(self.username_title)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.app_header)

        self.frame_9 = QFrame(self.CW)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"assets/icon/add-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"assets/icon/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"assets/icon/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.horizontalSpacer_3 = QSpacerItem(837, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u"assets/icon/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame_9)

        self.TW = QTabWidget(self.CW)
        self.TW.setObjectName(u"TW")
        self.TW.setFont(font)
        self.tab_Home = QWidget()
        self.tab_Home.setObjectName(u"tab_Home")
        self.verticalLayout_4 = QVBoxLayout(self.tab_Home)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.tab_Home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SA1 = QScrollArea(self.frame_2)
        self.SA1.setObjectName(u"SA1")
        self.SA1.setFrameShadow(QFrame.Plain)
        self.SA1.setWidgetResizable(True)
        self.SAWC1 = QWidget()
        self.SAWC1.setObjectName(u"SAWC1")
        self.SAWC1.setGeometry(QRect(0, 0, 627, 384))
        self.verticalLayout_5 = QVBoxLayout(self.SAWC1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.SAWC1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(37)
        self.formLayout_2.setVerticalSpacing(8)
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_11 = QLineEdit(self.frame_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_11)

        self.lineEdit_2 = QLabel(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lineEdit_2)

        self.lineEdit_10 = QLineEdit(self.frame_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_10)

        self.lineEdit_3 = QLabel(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lineEdit_3)

        self.lineEdit_12 = QLineEdit(self.frame_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_12)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.SAWC1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(20)
        self.formLayout_3.setVerticalSpacing(8)
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_17)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_19)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_25)

        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_26)

        self.lineEdit_6 = QLineEdit(self.frame_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_28 = QLabel(self.frame_5)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_28)

        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.label_29)

        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_30)

        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.label_31)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_35)

        self.lineEdit_7 = QLineEdit(self.frame_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lineEdit_7)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.SA1.setWidget(self.SAWC1)

        self.horizontalLayout_2.addWidget(self.SA1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_4 = QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(8)
        self.formLayout_4.setContentsMargins(18, -1, 18, 20)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setClearButtonEnabled(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setClearButtonEnabled(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_5)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_5 = QFormLayout(self.groupBox_3)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(10)
        self.formLayout_5.setVerticalSpacing(8)
        self.formLayout_5.setContentsMargins(18, -1, 18, 20)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setClearButtonEnabled(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_9 = QLineEdit(self.groupBox_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setClearButtonEnabled(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)


        self.verticalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.SA2 = QScrollArea(self.tab_Home)
        self.SA2.setObjectName(u"SA2")
        self.SA2.setFrameShadow(QFrame.Plain)
        self.SA2.setWidgetResizable(True)
        self.SAWC2 = QWidget()
        self.SAWC2.setObjectName(u"SAWC2")
        self.SAWC2.setGeometry(QRect(0, 0, 939, 396))
        self.verticalLayout_7 = QVBoxLayout(self.SAWC2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.SAWC2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_6)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(8)
        self.label_39 = QLabel(self.frame_6)
        self.label_39.setObjectName(u"label_39")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_39)

        self.label_40 = QLabel(self.frame_6)
        self.label_40.setObjectName(u"label_40")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_40)

        self.label_46 = QLabel(self.frame_6)
        self.label_46.setObjectName(u"label_46")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_46)

        self.lineEdit_15 = QLineEdit(self.frame_6)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_15)

        self.label_41 = QLabel(self.frame_6)
        self.label_41.setObjectName(u"label_41")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_41)

        self.lineEdit_13 = QLineEdit(self.frame_6)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_42 = QLabel(self.frame_6)
        self.label_42.setObjectName(u"label_42")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_42)

        self.label_43 = QLabel(self.frame_6)
        self.label_43.setObjectName(u"label_43")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_43)

        self.label_44 = QLabel(self.frame_6)
        self.label_44.setObjectName(u"label_44")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_44)

        self.label_48 = QLabel(self.frame_6)
        self.label_48.setObjectName(u"label_48")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_48)

        self.label_47 = QLabel(self.frame_6)
        self.label_47.setObjectName(u"label_47")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_47)

        self.lineEdit_16 = QLineEdit(self.frame_6)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setClearButtonEnabled(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_16)

        self.label_49 = QLabel(self.frame_6)
        self.label_49.setObjectName(u"label_49")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_49)

        self.label_50 = QLabel(self.frame_6)
        self.label_50.setObjectName(u"label_50")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_50)

        self.label_45 = QLabel(self.frame_6)
        self.label_45.setObjectName(u"label_45")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_14 = QLineEdit(self.frame_6)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setClearButtonEnabled(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_14)

        self.label_51 = QLabel(self.frame_6)
        self.label_51.setObjectName(u"label_51")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_51)

        self.lineEdit_17 = QLineEdit(self.frame_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setClearButtonEnabled(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_17)

        self.label_52 = QLabel(self.frame_6)
        self.label_52.setObjectName(u"label_52")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_52)

        self.label_53 = QLabel(self.frame_6)
        self.label_53.setObjectName(u"label_53")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.label_53)

        self.label_54 = QLabel(self.frame_6)
        self.label_54.setObjectName(u"label_54")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_54)

        self.lineEdit_18 = QLineEdit(self.frame_6)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setClearButtonEnabled(True)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_18)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.SA2.setWidget(self.SAWC2)

        self.verticalLayout_4.addWidget(self.SA2)

        self.TW.addTab(self.tab_Home, "")
        self.tab_Profile = QWidget()
        self.tab_Profile.setObjectName(u"tab_Profile")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Profile)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_11 = QFrame(self.tab_Profile)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.pushButton_5 = QPushButton(self.frame_11)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"border-radius: 25px;\n"
"border: 2px solid black;")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(48, 48))

        self.verticalLayout_8.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame = QFrame(self.tab_Profile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_8 = QFrame(self.tab_Profile)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(854, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(110, 0))
        self.pushButton_7.setMaximumSize(QSize(110, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"assets/icon/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.btn_UserDataSave = QPushButton(self.frame_8)
        self.btn_UserDataSave.setObjectName(u"btn_UserDataSave")
        icon6 = QIcon()
        icon6.addFile(u"assets/icon/tick.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_UserDataSave.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.btn_UserDataSave)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.verticalSpacer = QSpacerItem(20, 461, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.TW.addTab(self.tab_Profile, "")

        self.verticalLayout.addWidget(self.TW)

        self.frame_7 = QFrame(self.CW)
        self.frame_7.setObjectName(u"frame_7")
        font2 = QFont()
        font2.setFamily(u"Poppins Medium")
        font2.setPointSize(9)
        self.frame_7.setFont(font2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(633, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_7)

        Interface.setCentralWidget(self.CW)

        self.retranslateUi(Interface)

        self.TW.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Interface)
    # setupUi

    def retranslateUi(self, Interface):
        Interface.setWindowTitle(QCoreApplication.translate("Interface", u"Details Calculator SDRF", None))
        self.app_name.setText(QCoreApplication.translate("Interface", u"Details Calculator SDRF", None))
        self.username_title.setText(QCoreApplication.translate("Interface", u"User", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Interface", u"New", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Interface", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Interface", u"Open", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Interface", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("Interface", u"Save", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("Interface", u"Info", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Interface", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.label_13.setText(QCoreApplication.translate("Interface", u"Total Land of the Building:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Interface", u"Total Super Builtup area of the Building:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Interface", u"Flat Super Builtup area:", None))
        self.label_16.setText(QCoreApplication.translate("Interface", u"Proportiinate Share in land:", None))
        self.label_17.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_18.setText(QCoreApplication.translate("Interface", u"Proportionate Share in Decimals:", None))
        self.label_19.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_20.setText(QCoreApplication.translate("Interface", u"Govt Value of Flat:", None))
        self.label_25.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_26.setText(QCoreApplication.translate("Interface", u"Govt Value of Parking:", None))
        self.label_28.setText(QCoreApplication.translate("Interface", u"Govt Value of Proportionate Share in land:", None))
        self.label_29.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_30.setText(QCoreApplication.translate("Interface", u"Total Govt Value of the Flat:", None))
        self.label_31.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_35.setText(QCoreApplication.translate("Interface", u"Actual Consideration:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Interface", u"Govt. Rate", None))
        self.label_4.setText(QCoreApplication.translate("Interface", u"Rate per dec.:", None))
        self.label_5.setText(QCoreApplication.translate("Interface", u"Rate per sq. feet:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Interface", u"Stamp Duty |  Reg. Fee Percentage", None))
        self.label_6.setText(QCoreApplication.translate("Interface", u"Stamp:", None))
        self.label_7.setText(QCoreApplication.translate("Interface", u"Reg. Fee:", None))
        self.label_39.setText(QCoreApplication.translate("Interface", u"Stamp:", None))
        self.label_40.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_46.setText("")
        self.label_41.setText(QCoreApplication.translate("Interface", u"Previous Stamp Paid:", None))
        self.label_42.setText(QCoreApplication.translate("Interface", u"Net Stamp:", None))
        self.label_43.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_44.setText(QCoreApplication.translate("Interface", u"Reg. Fee:", None))
        self.label_48.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_47.setText("")
        self.label_49.setText(QCoreApplication.translate("Interface", u"Net. Reg Fee:", None))
        self.label_50.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_45.setText(QCoreApplication.translate("Interface", u"LLR:", None))
        self.label_51.setText(QCoreApplication.translate("Interface", u"Score:", None))
        self.label_52.setText(QCoreApplication.translate("Interface", u"Grand Total:", None))
        self.label_53.setText(QCoreApplication.translate("Interface", u"--", None))
        self.label_54.setText(QCoreApplication.translate("Interface", u"Adv. Fee:", None))
        self.TW.setTabText(self.TW.indexOf(self.tab_Home), QCoreApplication.translate("Interface", u"Home", None))
        self.label_8.setText(QCoreApplication.translate("Interface", u"Profile Image:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("Interface", u"Choose Image", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Interface", u"User:", None))
        self.pushButton_7.setText(QCoreApplication.translate("Interface", u" Delete User ", None))
        self.btn_UserDataSave.setText(QCoreApplication.translate("Interface", u" Save", None))
        self.TW.setTabText(self.TW.indexOf(self.tab_Profile), QCoreApplication.translate("Interface", u"Profile", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Interface", u"<html><head/><body><p>Designed &amp; Developed by: <span style=\" font-weight:600;\">Pratham Raj Singh</span></p><p>Visit: <span style=\" font-weight:600;\"><a href=\"imprs.vercel.app\">imprs.vercel.app</a></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Interface", u"Designed & Developed by: Pratham Raj Singh", None))
        self.label_3.setText(QCoreApplication.translate("Interface", u"Version: ---", None))
    # retranslateUi

