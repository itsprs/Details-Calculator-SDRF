import sys, json, shutil

from PIL import Image, ImageDraw
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from PySide2.QtCore import QFile, QStandardPaths, QProcess, QRegExp, QDir
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

        self.pushButton_3.clicked.connect(lambda: self.TW.setCurrentWidget(self.tab_Profile))
        self.pushButton_5.clicked.connect(lambda: self.pushButton_5.setIcon(QIcon(selectAvatar())))
        self.btn_UserDataSave.clicked.connect(self.saveUserData)
        self.pushButton_7.clicked.connect(self.deleteUserData)

    def closeEvent(self, event):
        self.deinitialize()
        event.accept()

    def initialize(self):
        if readData('isMaximized', 'userdata/userdata.json'):
            self.showMaximized()
        self.renderUserData()

        if not QFile.exists('userdata/recent.json'):
            self.update()
        else:
            recentData = readWholeData('userdata/recent.json')
            lineEdits = [
                'lineEdit_6', 'lineEdit_7', 'lineEdit_4', 'lineEdit_5',
                'lineEdit_8', 'lineEdit_9', 'lineEdit_13', 'lineEdit_14',
                'lineEdit_15', 'lineEdit_16', 'lineEdit_17', 'lineEdit_18',
                'lineEdit_10', 'lineEdit_11', 'lineEdit_12'
            ]
            for key in lineEdits:
                getattr(self, key).setText(recentData.get(key, ''))
            self.update()

    def deinitialize(self):
        writeData('isMaximized', self.isMaximized(), 'userdata/userdata.json')

        lineEdit_keys = [
            'lineEdit_6', 'lineEdit_7', 'lineEdit_4', 'lineEdit_5',
            'lineEdit_8', 'lineEdit_9', 'lineEdit_13', 'lineEdit_14',
            'lineEdit_15', 'lineEdit_16', 'lineEdit_17', 'lineEdit_18',
            'lineEdit_10', 'lineEdit_11', 'lineEdit_12'
        ]
        
        recentData = {key: getattr(self, key).text() for key in lineEdit_keys}
        writeWholeData(recentData, 'userdata/recent.json')

    # ---
    
    def update(self):
        try:
            en = all([self.lineEdit_11.text(), self.lineEdit_10.text(), self.lineEdit_12.text()])
            enLineEdits = [
                self.lineEdit_6, self.lineEdit_7, self.lineEdit_4, self.lineEdit_5,
                self.lineEdit_8, self.lineEdit_9, self.lineEdit_13, self.lineEdit_14,
                self.lineEdit_15, self.lineEdit_16, self.lineEdit_17, self.lineEdit_18
            ]
            for line_edit in enLineEdits:
                line_edit.setEnabled(en)
            
            if en:
                a = (float(self.lineEdit_11.text()) / float(self.lineEdit_10.text())) * float(self.lineEdit_12.text())
                b = a / 435.52
                self.label_17.setText(f'{a:.2f}')
                self.label_19.setText(f'{b:.2f}')
            else:
                self.label_17.setText('--')
                self.label_19.setText('--')

            self.label_29.setText(f'{float(self.lineEdit_4.text()) * b:.2f}' if self.lineEdit_4.text() else '--')
            self.label_25.setText(f'{float(self.lineEdit_12.text()) * float(self.lineEdit_5.text()):.2f}' if self.lineEdit_5.text() else '--')

            if self.lineEdit_6.text() and self.lineEdit_4.text() and self.lineEdit_5.text():
                self.label_31.setText(f'{float(self.label_25.text()) + float(self.label_29.text()) + float(self.lineEdit_6.text()):.2f}')
            else:
                self.label_31.setText('--')

            if self.lineEdit_7.text() and self.lineEdit_8.text():
                c = (float(self.lineEdit_8.text()) / 100) * float(self.lineEdit_7.text())
                self.label_40.setText(f'{c:.2f}')
            else:
                self.label_40.setText('--')

            if self.lineEdit_15.text() and self.lineEdit_13.text() and self.lineEdit_7.text() and self.lineEdit_8.text():
                self.label_43.setText(f'{(c + float(self.lineEdit_15.text())) - float(self.lineEdit_13.text()):.2f}')
            else:
                self.label_43.setText('--')

            if self.lineEdit_9.text() and self.lineEdit_7.text():
                d = (float(self.lineEdit_9.text()) / 100) * float(self.lineEdit_7.text())
                self.label_48.setText(f'{d:.2f}')
            else:
                self.label_48.setText('--')

            if self.lineEdit_16.text() and self.lineEdit_9.text() and self.lineEdit_7.text():
                self.label_50.setText(f'{d + float(self.lineEdit_16.text()):.2f}')
            else:
                self.label_50.setText('--')

            if all([self.lineEdit_15.text(), self.lineEdit_13.text(), self.lineEdit_16.text(), self.lineEdit_14.text(), self.lineEdit_17.text()]):
                gt = (c + float(self.lineEdit_15.text())) - float(self.lineEdit_13.text()) + d + float(self.lineEdit_16.text()) + float(self.lineEdit_14.text()) + float(self.lineEdit_17.text())
                self.label_53.setText(f'{gt:.2f}')
            else:
                self.label_53.setText('--')    

        except Exception as e:
            print(e)
            pass

    # ---

    def renderUserData(self):
        userData = readWholeData('userdata/userdata.json')
        self.username_title.setText(userData['name'])
        self.lineEdit.setText(userData['name'])
        self.pushButton_3.setIcon(QIcon(userData['avatar']))
        self.pushButton_5.setIcon(QIcon(userData['avatar']))

    def saveUserData(self):
        if len(self.lineEdit.text().strip()):
            writeData('name', self.lineEdit.text().strip(), 'userdata/userdata.json')
            self.renderUserData()
            self.TW.setCurrentWidget(self.tab_Home)
        else:
            self.lineEdit.clear()

    def deleteUserData(self):
        if QFile.exists('userdata'):
            shutil.rmtree('userdata')
            self.restartApplication()

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
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]*"), self.lineEdit))

        self.pushButton.clicked.connect(self.createUser)
        self.pushButton_2.clicked.connect(lambda: self.pushButton_2.setIcon(QIcon(selectAvatar())))

    def createUser(self):
        if len(self.lineEdit.text().strip()) > 0:
            avtpath = ''

            QDir().mkdir('userdata')
            if QFile.exists('temp.png'):
                QFile.rename('temp.png', 'userdata/profile.png')
                avtpath = 'userdata/profile.png'
            else:
                avtpath = 'assets/default.webp'

            initialData = {
                'name': self.lineEdit.text().strip(),
                'isMaximized': True,
                'avatar': avtpath
            }

            writeWholeData(initialData, 'userdata/userdata.json')
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
        if QFile.exists('userdata'):
            self.showApp()
        else:
            if QFile.exists('temp.png'):
                QFile.remove('temp.png')
            self.window = Startup()
            self.window.show()
        sys.exit(self.app.exec_())

# ---
        
def selectAvatar():
    file = QFileDialog.getOpenFileName(None, 'Select Image', QStandardPaths.writableLocation(QStandardPaths.PicturesLocation), 'Image Files (*.png *.jpg *.jpeg)')[0]
    if file:
        if not QFile.exists('userdata'):
            cropCircle(file, 'temp.png')
            return 'temp.png'
        else:
            cropCircle(file, 'userdata/profile.png')
            writeData('avatar', 'userdata/profile.png', 'userdata/userdata.json')
            return 'userdata/profile.png'
    else:
        return 'assets/default.webp'

def cropCircle(image_path, output_path):
    image = Image.open(image_path)
    width, height = image.size
    min_dimension = min(width, height)
    left = (width - min_dimension) // 2
    top = (height - min_dimension) // 2
    right = left + min_dimension
    bottom = top + min_dimension
    square_image = image.crop((left, top, right, bottom))
    mask = Image.new('L', (min_dimension, min_dimension), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, min_dimension, min_dimension), fill=255)
    result = Image.new('RGBA', (min_dimension, min_dimension))
    result.paste(square_image, (0, 0), mask)
    result.save(output_path, format="PNG")

# File Handling >

def readData(key, file):
    with open(file, 'r') as f:
        return json.load(f).get(key, None)

def writeData(key, value, file):
    with open(file, 'r+') as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

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
