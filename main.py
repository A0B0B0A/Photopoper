from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from ui import Ui_MainWindow

import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.workdir = None  
        self.filenames = None
        self.image = None

        self.ui.file.clicked.connect(self.choose_folder)

    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_list_image()
        except:
            error = QMessageBox()
            error.setText("Error")
            error.exec_()

    def show_list_image(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)
        self.ui.listpictures.clear()
        self.ui.listpictures.addItems(images)

#    def show_picture(self):









app = QApplication([])
ex = Widget()
ex.show()
app.exec_()




# python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py

# with Image.open('beer.jpg') as original:
#     pic_gray= original.convert("L")
#     pic_gray.save("black.jpg")
#     pic_gray.show() 