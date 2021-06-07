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

        self.loadingText = QLabel("<font color=\"white\"> Loading Game...", self)
        self.loadingText.setGeometry(QRect(137, 225, 685, 125))
        loadingFont = QFont()
        loadingFont.setFamily(u"Yrsa")
        loadingFont.setPointSize(80)
        loadingFont.setBold(True)
        loadingFont.setItalic(True)
        loadingFont.setWeight(75)
        self.loadingText.setFont(loadingFont)
        self.loadingText.setAlignment(Qt.AlignCenter)

        self.gameCore = GameCore(self)
        self.startTimer = QTimer(self)
        self.startTimer.setInterval(3000)
        self.startTimer.timeout.connect(self.startGame)
        self.startTimer.start()

    def startGame(self):
        self.gameCore.startGame()

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(QRect(0, 0, self.gameCore.geometry().width(), self.gameCore.geometry().height()),
                       self.gameCore.background)

    def keyPressEvent(self, event: QKeyEvent):
        self.gameCore.keyEventDist(event, True)

    def keyReleaseEvent(self, event: QKeyEvent):
        self.gameCore.keyEventDist(event, False)


app = QApplication(sys.argv)
win = Window()
win.show()
app.exec()
