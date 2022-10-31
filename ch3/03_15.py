# PyQt 윈도우 꾸미기(03-5)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 400)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()