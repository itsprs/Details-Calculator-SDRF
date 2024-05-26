import sys, os, json, shutil
from PIL import Image, ImageDraw
from xhtml2pdf import pisa
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import QFile, QStandardPaths, QProcess, QRegExp, QDir
from PySide2.QtGui import QFontDatabase, QIcon, QDoubleValidator, QRegExpValidator, QTextCursor, QTextDocument
from PySide2.QtPrintSupport import QPrinter, QPrintDialog

from ui_interface import Ui_Interface
from ui_startup import Ui_Startup
from ui_about import Ui_About

# Details >

class AppDetails:
    def __init__(self):
        self.app_name = "Details Calculator SDRF"
        self.app_version = "1.0.0"
        self.app_developer = "Pratham Raj Singh"
        self.app_developer_website = "imprs.vercel.app"
        self.app_description = "Details Calculator SDRF is a desktop application designed to calculate and manage detailed property and financial information related to real estate transactions. It provides a user-friendly interface for inputting and calculating various parameters such as the land area, built-up area, government values, stamp duty, and registration fees."

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

        self.pushButton_4.clicked.connect(self.show_AboutDialog)
        self.pushButton_3.clicked.connect(lambda: self.TW.setCurrentWidget(self.tab_Profile))
        self.pushButton_5.clicked.connect(lambda: self.pushButton_5.setIcon(QIcon(selectAvatar())))
        self.btn_UserDataSave.clicked.connect(self.saveUserData)
        self.pushButton_7.clicked.connect(self.deleteUserData)
        self.pushButton_2.clicked.connect(self.savePdf)
        self.pushButton.clicked.connect(self.printPdf)

    def closeEvent(self, event):
        self.deinitialize()
        event.accept()

    def initialize(self):
        if readData('isMaximized', 'userdata\\userdata.json'):
            self.showMaximized()
        self.renderUserData()

        if not QFile.exists(get_user_path('userdata\\recent.json')):
            self.update()
        else:
            recentData = readWholeData('userdata\\recent.json')
            lineEdits = [
                'lineEdit_6', 'lineEdit_7', 'lineEdit_4', 'lineEdit_5',
                'lineEdit_8', 'lineEdit_9', 'lineEdit_13', 'lineEdit_14',
                'lineEdit_15', 'lineEdit_16', 'lineEdit_17', 'lineEdit_18',
                'lineEdit_10', 'lineEdit_11', 'lineEdit_12', 'lineEdit_19',
            ]
            for key in lineEdits:
                getattr(self, key).setText(recentData.get(key, ''))
            self.update()

    def deinitialize(self):
        writeData('isMaximized', self.isMaximized(), 'userdata\\userdata.json')

        lineEdit_keys = [
            'lineEdit_6', 'lineEdit_7', 'lineEdit_4', 'lineEdit_5',
            'lineEdit_8', 'lineEdit_9', 'lineEdit_13', 'lineEdit_14',
            'lineEdit_15', 'lineEdit_16', 'lineEdit_17', 'lineEdit_18',
            'lineEdit_10', 'lineEdit_11', 'lineEdit_12', 'lineEdit_19'
        ]
        
        recentData = {key: getattr(self, key).text() for key in lineEdit_keys}
        writeWholeData(recentData, 'userdata\\recent.json')

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
                self.label_17.setText(f'{a}')
                self.label_19.setText(f'{b}')
            else:
                self.label_17.setText('--')
                self.label_19.setText('--')

            self.label_29.setText(f'{float(self.lineEdit_4.text()) * b}' if self.lineEdit_4.text() else '--')
            self.label_25.setText(f'{float(self.lineEdit_12.text()) * float(self.lineEdit_5.text()):}' if self.lineEdit_5.text() else '--')

            if self.lineEdit_6.text() and self.lineEdit_4.text() and self.lineEdit_5.text():
                self.label_31.setText(f'{float(self.label_25.text()) + float(self.label_29.text()) + float(self.lineEdit_6.text())}')
            else:
                self.label_31.setText('--')

            if self.lineEdit_7.text() and self.lineEdit_8.text():
                c = (float(self.lineEdit_8.text()) / 100) * float(self.lineEdit_7.text())
                self.label_40.setText(f'{c}')
            else:
                self.label_40.setText('--')

            if self.lineEdit_15.text() and self.lineEdit_13.text() and self.lineEdit_7.text() and self.lineEdit_8.text():
                self.label_43.setText(f'{(c + float(self.lineEdit_15.text())) - float(self.lineEdit_13.text())}')
            else:
                self.label_43.setText('--')

            if self.lineEdit_9.text() and self.lineEdit_7.text():
                d = (float(self.lineEdit_9.text()) / 100) * float(self.lineEdit_7.text())
                self.label_48.setText(f'{d}')
            else:
                self.label_48.setText('--')

            if self.lineEdit_16.text() and self.lineEdit_9.text() and self.lineEdit_7.text():
                self.label_50.setText(f'{d + float(self.lineEdit_16.text())}')
            else:
                self.label_50.setText('--')

            if all([self.lineEdit_15.text(), self.lineEdit_13.text(), self.lineEdit_16.text(), self.lineEdit_14.text(), self.lineEdit_17.text()]):
                gt = (c + float(self.lineEdit_15.text())) - float(self.lineEdit_13.text()) + d + float(self.lineEdit_16.text()) + float(self.lineEdit_14.text()) + float(self.lineEdit_17.text())
                self.label_53.setText(f'{gt}')
            else:
                self.label_53.setText('--')    

        except Exception as e:
            print(e)
            pass

    # ---

    def con_template(self):
        return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        line-height: 1;
                    }}
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }}
                    th, td {{
                        border: 1px solid
                        #dddddd;
                        text-align: left;
                        padding: 5px;
                        width: auto;
                    }}
                    th {{
                        background-color:
                        #f2f2f2;
                    }}
                </style>
            </head>
            <body>
                <h1>Detailed Report</h1>
                <table>
                    <tr>
                        <th>Name of the Building</th>
                        <td>{self.lineEdit_19.text()}</td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <th>Total Land of the Building (sq. ft.)</th>
                        <td>{self.lineEdit_11.text()}</td>
                    </tr>
                    <tr>
                        <th>Total Super Builtup area of the Building (sq. ft.)</th>
                        <td>{self.lineEdit_10.text()}</td>
                    </tr>
                    <tr>
                        <th>Flat Super Builtup area (sq. ft.)</th>
                        <td>{self.lineEdit_12.text()}</td>
                    </tr>
                    <tr>
                        <th>Proportionate Share in land (sq. ft.)</th>
                        <td>{self.label_17.text()}</td>
                    </tr>
                    <tr>
                        <th>Proportionate Share in Decimals</th>
                        <td>{self.label_19.text()}</td>
                    </tr>
                    <tr>
                        <th>Govt Value of Flat (per sq. ft.)</th>
                        <td>{self.label_25.text()}</td>
                    </tr>
                    <tr>
                        <th>Govt Value of Parking (per sq. ft.)</th>
                        <td>{self.lineEdit_5.text()}</td>
                    </tr>
                    <tr>
                        <th>Govt Value of Proportionate Share in land (per sq. ft.)</th>
                        <td>{self.label_29.text()}</td>
                    </tr>
                    <tr>
                        <th>Total Govt Value of the Flat</th>
                        <td>{self.label_31.text()}</td>
                    </tr>
                    <tr>
                        <th>Actual Consideration</th>
                        <td>{self.lineEdit_7.text()}</td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <th>Rate per dec.</th>
                        <td>{self.lineEdit_4.text()}</td>
                    </tr>
                    <tr>
                        <th>Rate per sq. feet</th>
                        <td>{self.lineEdit_5.text()}</td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <th>Stamp</th>
                        <td>{self.lineEdit_8.text()}</td>
                    </tr>
                    <tr>
                        <th>Reg. Fee</th>
                        <td>{self.lineEdit_9.text()}</td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <th>Stamp</th>
                        <td>{self.label_40.text()} + {self.lineEdit_15.text()}</td>
                    </tr>
                    <tr>
                        <th>Previous Stamp Paid</th>
                        <td>{self.lineEdit_13.text()}</td>
                    </tr>
                    <tr>
                        <th>Net Stamp</th>
                        <td>{self.label_43.text()}</td>
                    </tr>
                    <tr>
                        <th>Reg. Fee</th>
                        <td>{self.label_48.text()} + {self.lineEdit_16.text()}</td>
                    </tr>
                    <tr>
                        <th>Net. Reg Fee</th>
                        <td>{self.label_50.text()}</td>
                    </tr>
                    <tr>
                        <th>LLR</th>
                        <td>{self.lineEdit_14.text()}</td>
                    </tr>
                    <tr>
                        <th>Score</th>
                        <td>{self.lineEdit_17.text()}</td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <th>Grand Total</th>
                        <td>{self.label_53.text()}</td>
                    </tr>
                    <tr>
                        <th>Adv. Fee</th>
                        <td>{self.lineEdit_18.text()}</td>
                    </tr>
                </table>
            </body>
            </html>
        """
    
    def savePdf(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save PDF", "sdrf-details.pdf", "PDF Files (*.pdf);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'wb') as f:
                    pisa.CreatePDF(self.con_template(), dest=f)
                QMessageBox.information(self, "PDF Saved", f"PDF file saved successfully.\n\nFile Path:\n {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "PDF Error", f"An error occurred while saving the PDF file:\n{str(e)}")

    def printPdf(self):
        try:
            printer = QPrinter()
            printer.setPrinterName("")
            printer.setOutputFileName("")
            printer.setOutputFormat(QPrinter.NativeFormat)
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                document = QTextDocument()
                cursor = QTextCursor(document)
                cursor.insertHtml(self.con_template())
                document.print_(printer)
                QMessageBox.information(self, "Print", f"Detailed Report printed successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Print Error", f"An error occurred while printing:\n{str(e)}")

    # ---

    def show_AboutDialog(self):
        about_dialog = About(self)
        about_dialog.exec_()

    def renderUserData(self):
        userData = readWholeData('userdata\\userdata.json')
        self.username_title.setText(userData['name'])
        self.lineEdit.setText(userData['name'])
        self.pushButton_3.setIcon(QIcon(userData['avatar']))
        self.pushButton_5.setIcon(QIcon(userData['avatar']))

    def saveUserData(self):
        if len(self.lineEdit.text().strip()):
            writeData('name', self.lineEdit.text().strip(), 'userdata\\userdata.json')
            self.renderUserData()
            QMessageBox.information(self, "User Saved", f"User data saved successfully.")
            self.TW.setCurrentWidget(self.tab_Home)
        else:
            self.lineEdit.clear()

    def deleteUserData(self):
        if QFile.exists(get_user_path('userdata')):
            shutil.rmtree(get_user_path('userdata'))
            self.restartApplication()

    def restartApplication(self):
        QApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)

# Functions >
        
    def setDobValidator(self, list_le):
        [line_edit.setValidator(QDoubleValidator()) for line_edit in list_le]

# Other UI >

class About(QDialog, Ui_About):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(f'About - {app_details.app_name}')
        self.label_2.setText(app_details.app_name)
        self.label_4.setText(app_details.app_description)
        self.label_8.setText(f'Version: {app_details.app_version}')
        self.label_5.setText(app_details.app_developer)

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

            QDir().mkdir(os.path.join(os.path.expanduser("~"), "Details Calculator SDRF"))
            QDir().mkdir(get_user_path('userdata'))
            if QFile.exists(get_user_path('temp.png')):
                QFile.rename(get_user_path('temp.png'), get_user_path('userdata\\profile.png'))
                avtpath = get_user_path('userdata\\profile.png')
            else:
                avtpath = 'assets/default.webp'

            initialData = {
                'name': self.lineEdit.text().strip(),
                'isMaximized': True,
                'avatar': avtpath
            }

            writeWholeData(initialData, get_user_path('userdata\\userdata.json'))
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
        if QFile.exists(get_user_path('userdata')):
            self.showApp()
        else:
            if QFile.exists(get_user_path('temp.png')):
                QFile.remove(get_user_path('temp.png'))
            self.window = Startup()
            self.window.show()
        sys.exit(self.app.exec_())

# ---
        
def selectAvatar():

    file_dialog = QFileDialog(None)
    file_dialog.setWindowIcon(QIcon('assets/icon.ico'))
    file = file_dialog.getOpenFileName(None, 'Select Image', QStandardPaths.writableLocation(QStandardPaths.PicturesLocation), 'Image Files (*.png *.jpg *.jpeg)')[0]

    if file:
        if not QFile.exists(get_user_path('userdata')):
            QDir().mkdir(os.path.join(os.path.expanduser("~"), "Details Calculator SDRF"))
            cropCircle(file, get_user_path('temp.png'))
            return get_user_path('temp.png')
        else:
            cropCircle(file, get_user_path('userdata\\profile.png'))
            writeData('avatar', get_user_path('userdata\\profile.png'), get_user_path('userdata\\userdata.json'))
            return get_user_path('userdata\\profile.png')
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

def get_user_path(relative_path):
    return os.path.join(os.path.expanduser("~"), "Details Calculator SDRF", relative_path)

def readData(key, file):
    with open(get_user_path(file), 'r') as f:
        return json.load(f).get(key, None)

def writeData(key, value, file):
    with open(get_user_path(file), 'r+') as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def readWholeData(file):
    with open(get_user_path(file), 'r') as f:
        return json.load(f)

def writeWholeData(data, file):
    with open(get_user_path(file), 'w') as f:
        json.dump(data, f, indent=4)

# Main >

if __name__ == '__main__':
    main_app = MainApplication()
    main_app.start()
