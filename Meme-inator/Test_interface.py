import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PIL import Image, ImageDraw, ImageFont
import random, os

fileName = ""

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Choose meme'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.Choose_Meme()
        
        self.show()
    
    def Choose_Meme(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

        for i in range(10):

            # gfg_logo.jpeg image opened using
            # open function and assigned to variable named img
            img = Image.open(""+fileName)
            width, height = img.size
            #height = int(height*100/width)
            #width = 100
            #img = img.resize((width, height))

            # Image is converted into editable form using
            # Draw function and assigned to d1
            d1 = ImageDraw.Draw(img)
 
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
                d1.text((random.randint(0, width-int(len(txt)*font/2)), random.randint(0, height-font)), txt, fill =(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),font=myFont)

            # show and save the image
            # img.show()
    
            img.save("./RESULTS/E_results{}.png".format(i))
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    #sys.exit(app.exec_())
