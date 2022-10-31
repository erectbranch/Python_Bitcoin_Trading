# PyQt Qt Designer(03-6)

import os
import pykorbit    # 비트코인 현재가를 쉽게 얻을 수 있는 pykorbit 모듈
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic

ui_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(ui_path, "window.ui"))[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)    # setupUi(): QT Designer에서 만든 클래스들을 초기화한다.
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        # print(price)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()