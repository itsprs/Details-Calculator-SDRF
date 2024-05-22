import sys, json
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from PySide2.QtCore import QFile, QStandardPaths, QProcess, QRegExp
from PySide2.QtGui import QFontDatabase, QIcon, QDoubleValidator, QRegExpValidator

from ui_interface import Ui_Interface
from ui_startup import Ui_Startup

# Details >

class AppDetails:
    def __init__(self):
        self.app_name = "Details Calculator SDRF"
        self.app_version = "0.0.1"
        self.app_developer = "Pratham Raj Singh"
        self.app_developer_website = "imprs.vercel.app"

app_details = AppDetails()

# Application >

class App(QMainWindow, Ui_Interface):
    
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(app_details.app_name)
        self.app_name.setText(app_details.app_name)
        self.label_2.setText(f'Designed & Developed by: {app_details.app_developer}')
        self.label_3.setText(f'Version: {app_details.app_version}')
        self.TW.setCurrentWidget(self.tab_Home)
        self.setDobValidator([self.lineEdit_11, self.lineEdit_10, self.lineEdit_12, self.lineEdit_6, self.lineEdit_7, self.lineEdit_4, self.lineEdit_5, self.lineEdit_8, self.lineEdit_9, self.lineEdit_13, self.lineEdit_14, self.lineEdit_15, self.lineEdit_16, self.lineEdit_17, self.lineEdit_18])
        self.initialize()

        for i in [self.lineEdit_11, self.lineEdit_10, self.lineEdit_12, self.lineEdit_6, self.lineEdit_7, self.lineEdit_4, self.lineEdit_5, self.lineEdit_8, self.lineEdit_9, self.lineEdit_13, self.lineEdit_14, self.lineEdit_15, self.lineEdit_16, self.lineEdit_17, self.lineEdit_18]:
            i.textChanged.connect(self.update)

    def closeEvent(self, event):
        pass

    def initialize(self):
        pass

    # ---
    
    def update(self):
        pass

    # ---

    def restartApplication(self):
        QApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)

# Functions >
        
    def setDobValidator(self, list_le):
        [line_edit.setValidator(QDoubleValidator()) for line_edit in list_le]

# Other UI >

class Startup(QDialog, Ui_Startup):

    def __init__(self, parent=None):
        super(Startup, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(app_details.app_name)
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z]*"), self.lineEdit))

    def createUser(self):
        self.close()
        main_app.showApp()

# Main Application >

class MainApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)
        QFontDatabase.addApplicationFont('assets/font/Poppins-Medium.ttf')
        QFontDatabase.addApplicationFont('assets/font/Poppins-Regular.ttf')
        self.window = None

    def showApp(self):
        self.window = App()
        self.window.show()

    def start(self):
        if QFile.exists('userdata.json'):
            self.showApp()
        else:
            self.window = Startup()
            self.window.show()
        sys.exit(self.app.exec_())

# File Handling >

def readWholeData(file):
    with open(file, 'r') as f:
        return json.load(f)

def writeWholeData(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Main >

if __name__ == '__main__':
    main_app = MainApplication()
    main_app.start()
