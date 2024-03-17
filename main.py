from PIL import Image, ImageFilter
from ui import Ui_Photopop
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QInputDialog

class Widget(Ui_Photopop):
    def   __init__(self):
        super().__init__()  
        self.ui = Ui_Photopop()
        self.ui.setupUi(self)
        
app = QApplication([])


ex = Widget()
ex.show()
app.exec_()
# with Image.open('beer.jpg') as original:
#     pic_gray= original.convert("L")
#     pic_gray.save("black.jpg")
#     pic_gray.show() 