from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from GameCore import GameCore
from Utils.Resloader import resource_path
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(960, 600)
        self.setWindowTitle("Asteroids")
        self.setWindowIcon(QIcon(resource_path("Assets/roid.png")))

        self.gameCore = GameCore(self)
        self.startTimer = QTimer(self)
        self.startTimer.setInterval(1000)
        self.startTimer.timeout.connect(self.startGame)
        self.startTimer.start()

    def startGame(self):
        self.gameCore.startGame()

    def keyPressEvent(self, event: QKeyEvent):
        self.gameCore.keyEventDist(event, True)

    def keyReleaseEvent(self, event: QKeyEvent):
        self.gameCore.keyEventDist(event, False)


app = QApplication(sys.argv)
win = Window()
win.show()
app.exec()
