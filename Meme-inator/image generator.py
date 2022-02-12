# from PIL import Image, ImageDraw, ImageFont
# import random
# import csv
# import sys
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QMainWindow, QLabel
# from PyQt5.QtGui import QIcon, QPixmap
# from PyQt5 import QtGui, QtWidgets, QtPrintSupport

# # Subclass QMainWindow to customize your application's main window
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Meme_inator")

# #         button = QPushButton("Press Me!")
# #         button.setCheckable(True)
# #         button.clicked.connect(self.the_button_was_clicked)

# #         self.setFixedSize(QSize(500, 500))

# #         # Set the central widget of the Window.
# #         self.setCentralWidget(button)

# #     def the_button_was_clicked(self):
# #         print("clicked")

# # app = QApplication(sys.argv)

# # window = MainWindow()
# # window.show()

# # app.exec()
# # app.exec()
# # pathTemplates = "./TEMPLATE/"
# # pathResults = "./RESULTS/"
# # data=[]
# # for i in range(10):

# #     # gfg_logo.jpeg image opened using
# #     # open function and assigned to variable named img
# #     pathTemplate = pathTemplates + "bob.png"
# #     img = Image.open(pathTemplate)
# #     width, height = img.size
# #     #height = int(height*100/width)
# #     #width = 100
# #     #img = img.resize((width, height))

# #     # Image is converted into editable form using
# #     # Draw function and assigned to d1
# #     d1 = ImageDraw.Draw(img)
 
# #     # Font selection from the downloaded file
# #     myFont = ImageFont.truetype('./FONTS/IMPACT/Impact.ttf', 40)
    
    
# #     filename = "./CSVs/results.csv"
    
# #     # writing to csv file 
    
# #     for h in range(4):
# #         #Genère un texte aléatoire
# #         txt = ""
# #         for j in range(random.randint(1, 40)):
# #             txt = txt+chr(random.randint(32, 126))

# #         # Decide the text location, color and font
# #         d1.text((random.randint(0, width-len(txt*20)), random.randint(0, height-40)), txt, fill =(255, 255, 255),font=myFont)
# #     pathResult = pathResults + "V_results{}.png".format(i)
# #     img.save(pathResult)
# #     data.append([pathTemplate, pathResult ])
# # print(data)
# # with open(filename, 'w') as csvfile: 
# #     # creating a csv writer object 
# #     csvwriter = csv.writer(csvfile)        
# #     # writing the data rows 
# #     csvwriter.writerow(["meme", "template"])
# #     csvwriter.writerows(data)
# #     # show and save the image
# #     # img.show()
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#         button = QPushButton("Continuer")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         self.setFixedSize(QSize(500, 500))
#         # Set the central widget of the Window.
#         self.setCentralWidget(button)

#     def the_button_was_clicked(self):
#         self.close()



# class App(QtWidgets.QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.title = 'Meme_inator'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#         self.file = str()

#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.openFileNameDialog()
#         self.show()
    
#     def openFileNameDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
#         self.file = fileName
    
#     # def openFileNamesDialog(self):
#     #     options = QFileDialog.Options()
#     #     options |= QFileDialog.DontUseNativeDialog
#     #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
#     #     if files:
#     #         print(files)
    
#     # def saveFileDialog(self):
#     #     options = QFileDialog.Options()
#     #     options |= QFileDialog.DontUseNativeDialog
#     #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
#     #     if fileName:
#     #         print(fileName)
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog


class QImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.printer = QPrinter()
        self.scaleFactor = 0.0

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setVisible(False)

        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Image Viewer")
        self.resize(800, 600)

    def open(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollArea.setVisible(True)
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def print_(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def about(self):
        QMessageBox.about(self, "About Image Viewer",
                          "<p>The <b>Image Viewer</b> example shows how to combine "
                          "QLabel and QScrollArea to display an image. QLabel is "
                          "typically used for displaying text, but it can also display "
                          "an image. QScrollArea provides a scrolling view around "
                          "another widget. If the child widget exceeds the size of the "
                          "frame, QScrollArea automatically provides scroll bars.</p>"
                          "<p>The example demonstrates how QLabel's ability to scale "
                          "its contents (QLabel.scaledContents), and QScrollArea's "
                          "ability to automatically resize its contents "
                          "(QScrollArea.widgetResizable), can be used to implement "
                          "zooming and scaling features.</p>"
                          "<p>In addition the example shows how to use QPainter to "
                          "print an image.</p>")

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O", triggered=self.open)
        self.printAct = QAction("&Print...", self, shortcut="Ctrl+P", enabled=False, triggered=self.print_)
        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)
        self.zoomInAct = QAction("Zoom &In (25%)", self, shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
        self.zoomOutAct = QAction("Zoom &Out (25%)", self, shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)
        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+S", enabled=False, triggered=self.normalSize)
        self.fitToWindowAct = QAction("&Fit to Window", self, enabled=False, checkable=True, shortcut="Ctrl+F",
                                      triggered=self.fitToWindow)
        self.aboutAct = QAction("&About", self, triggered=self.about)
        self.aboutQtAct = QAction("About &Qt", self, triggered=qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    imageViewer = QImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())

    app2 = QApplication()
    imageViewer = QImageViewer()
    imageViewer.show()
    sys.exit(app2.exec_())