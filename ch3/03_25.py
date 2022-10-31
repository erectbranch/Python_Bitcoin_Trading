# PyQt Qt Designer(03-6)

import os
import pykorbit    # 비트코인 현재가를 쉽게 얻을 수 있는 pykorbit 모듈
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QTime

ui_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(ui_path, "window.ui"))[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.start(1000)                      # interval은 1초(1000): 즉 시계처럼 동작한다.
        self.timer.timeout.connect(self.inquiry)    # timeout: interval 마다 발생하는 이벤트

    def inquiry(self):
        cur_time = QTime.currentTime()              # 현재 시각을 받아온 뒤
        str_time = cur_time.toString("hh:mm:ss")    # 문자열 타입으로 변경한다.
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        # print(price)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()