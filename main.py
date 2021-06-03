from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Canvas import Canvas
from Utils.resloader import resource_path
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.setWindowTitle("Asteroids")
        self.setWindowIcon(QIcon(resource_path("Assets/roid.png")))

        self.canvas = Canvas(self)

    def tick(self):
        self.canvas.tick()



app = QApplication(sys.argv)
win = Window()

ticker = QTimer(win)
ticker.setInterval(0)
ticker.timeout.connect(win.tick)
ticker.start()

win.show()
app.exec()
