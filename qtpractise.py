import sys
import random
from PySide6.QtWidgets import  QApplication ,QMainWindow,QPushButton

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        btn2=QPushButton("?",self)
        btn=QPushButton("hi",self)

if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())