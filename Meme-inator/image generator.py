
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import os
from PIL import Image, ImageDraw, ImageFont
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 20, 761, 651))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.photo.setFont(font)
        self.photo.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo.setLineWidth(5)
        self.photo.setMidLineWidth(0)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect(10, 700, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browseFile.setFont(font)
        self.browseFile.setObjectName("browseFile")
        self.browseFile.clicked.connect(self.browse_file)

        self.chooseDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.chooseDirectory.setGeometry(QtCore.QRect(10, 750, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setPointSize(10)
        self.chooseDirectory.setFont(font)
        self.chooseDirectory.setObjectName("saveDirectory")
        self.chooseDirectory.clicked.connect(self.chooseFileDirectory)
        
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(790, 20, 791, 651))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.resultat.setFont(font)
        self.resultat.setFrameShape(QtWidgets.QFrame.Panel)
        self.resultat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.resultat.setLineWidth(5)
        self.resultat.setScaledContents(True)
        self.resultat.setObjectName("resultat")

        self.lancer = QtWidgets.QPushButton(self.centralwidget)
        self.lancer.setGeometry(QtCore.QRect(1300, 750, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.lancer.setFont(font)
        self.lancer.setObjectName("Lancer")
        self.lancer.clicked.connect(self.LancerProg)


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)   #Browse File
        self.lineEdit.setGeometry(QtCore.QRect(161, 700, 521, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.chosenDirectory = QtWidgets.QLineEdit(self.centralwidget)   #Browse File
        self.chosenDirectory.setGeometry(QtCore.QRect(161, 750, 521, 31))
        self.chosenDirectory.setObjectName("chosenDirectory")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Create a button in the window
        self.fileNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileNameButton.setGeometry(QtCore.QRect(10, 800, 150, 31))
        font = QtGui.QFont()
        self.fileNameButton.setFont(font)
        self.fileNameButton.setObjectName("fileNameButton")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.openDirectory = ""
        self.saveDirectory = "C:/Users/zevic/Documents/Hackaton/Meme-inator/Meme-inator/RESULTATS/"
        self.fileName = ""
        self.chooseDirectory = ""

        # Create textbox
        self.textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(161, 800, 521, 31))
        self.textbox.setObjectName("EnterFileName")
        # self.textbox.setAlignment(Qt.AlignBottom)
        # self.textbox.setFont(QFont("Arial",40))
        
        # connect button to function on_click
        self.fileNameButton.clicked.connect(self.chooseFileName)
        self.fileNameButton = ''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.photo.setText(_translate("MainWindow", "INPUT"))
        self.browseFile.setText(_translate("MainWindow", "Browse file"))
        self.lancer.setText(_translate("MainWindow", "LANCER"))
        self.resultat.setText(_translate("MainWindow", "OUTPUT"))
        self.chooseDirectory.setText(_translate("MainWindow", "Choose Directory"))
        self.fileNameButton.setText(_translate('MainWindow', 'File Name'))

    def browse_file(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(None, "Browse File", "", "JPEG (*.JPG *.jpg")[0]
        print(directory)
        pixmap =  QtGui.QPixmap(directory)
        self.photo.setPixmap(pixmap.scaled(self.photo.size()))
        self.lineEdit.setText('{}'.format(directory))
        self.directory = directory

    def chooseFileName(self):
        self.fileName = self.textbox.text()
        self.textbox.clear()


    def chooseFileDirectory(self):
        self.chooseDirectory = QtWidgets.QFileDialog.getExistingDirectory()      
        self.chosenDirectory.setText('{}'.format(self.chooseDirectory))

    def _set_text(self, text):
        return text

    def LancerProg(self):
        #Ouvre le template à utiliser et récupère sa taille
        a=0
        img1 = Image.open(self.directory)
        width, height = img1.size
        #Si voulu, le programme peut redimensioner l'image avec une largeur définie
        #larg = 100
        #height = int(height*larg/width)
        #width = larg
        height = 224
        width = 224
        img1 = img1.resize((width, height))
        # On transforme l'image en un format éditable
        d1 = ImageDraw.Draw(img1)
        img2 = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        d2 = ImageDraw.Draw(img2)
        # Font selection from the downloaded file
        #myFont = ImageFont.truetype('./FONTS/TEST/Kingthings_Trypewriter_2.ttf', 40)
        #print(".\FONTS\IMPACT"+chr(92)+random.choice(os.listdir(".\FONTS\IMPACT")))
        #myFont = ImageFont.truetype(".\FONTS\TEST"+chr(92)+random.choice(os.listdir(".\FONTS\TEST")), 40)
        for h in range(4):
            #Genère un texte aléatoire
            txt = ""
            for j in range(random.randint(1, 40)):
                txt = txt+chr(random.randint(32, 126))

            # Decide the text location, color and font
            font = int(width/20)
            myFont = ImageFont.truetype(".\FONTS\TEST"+chr(92)+random.choice(os.listdir(".\FONTS\TEST")), font)

            x = random.randint(0, width-int(len(txt)*font/2))
            y = random.randint(0, height-font)
            d1.text((x, y), txt, fill =(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),font=myFont)
            d2.text((x, y), txt, fill =(255, 255, 255),font=myFont)
        # show and save the image
        # img.show()
        img1.save(self.chooseDirectory + "/" + self.fileName + ".jpg")
        #img2.save("./MASKS/mask{}-{}.png".format(a, i))
        self.resultat.setPixmap(QtGui.QPixmap(os.path.realpath(self.chooseDirectory + "/" + self.fileName + ".jpg" )))
        #self.resultat.setPixmap(QtGui.QPixmap(os.path.realpath("C:/Users/zevic/Documents/Hackaton/Meme-inator/Meme-inator/TEMPLATE/Tem11.jpg" )))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
sys.exit(app.exec_())