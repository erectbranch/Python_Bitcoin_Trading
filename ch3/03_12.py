# PyQt 기초(03-4)

import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello")
label.show()
app.exec_()