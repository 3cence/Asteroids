from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from QtOverrides import *
from GameCore import GameCore
from Game.LoadingScreen import LoadingScreen
from Utils.Resloader import resource_path
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(960, 600)
        self.setWindowTitle("Asteroids")
        self.setWindowIcon(QIcon(resource_path("Assets/roid.png")))

        # Somehow, all this is for the loading text
        self.loadingText = QLabel(self)
        self.loadingSubtext = QLabel(self)
        self.loadingUptext = QLabel(self)
        self.loadingText.setGeometry(QRect(0, 225, 960, 125))
        self.loadingSubtext.setGeometry(QRect(0, 310, 960, 125))
        self.loadingUptext.setGeometry(QRect(0, 175, 960, 125))
        loadingFont = QFont()
        loadingFont.setFamily(u"Yrsa")
        loadingFont.setPointSize(80)
        loadingFont.setBold(True)
        loadingFont.setItalic(True)
        loadingFont.setWeight(75)
        self.loadingText.setFont(loadingFont)
        self.loadingText.setAlignment(Qt.AlignCenter)
        loadingFont.setPointSize(35)
        self.loadingSubtext.setFont(loadingFont)
        self.loadingSubtext.setAlignment(Qt.AlignCenter)
        self.loadingUptext.setFont(loadingFont)
        self.loadingUptext.setAlignment(Qt.AlignCenter)

        #Starting Screen
        self.loadingScreen = LoadingScreen(self)

        # Start the games engines
        self.gameCore = GameCore(self)
        self.startTimer = QTimer(self)
        self.startTimer.setInterval(2250)
        self.startTimer.timeout.connect(self.startGame)

        # self.startTimer.start()
        self.loadingText.setText("<font color=\"green\"> Loading Game...")
        self.loadingSubtext.setText("<font color=\"grey\"> Gimmie a Minute")


    def restartGame(self):
        self.gameCore.resetGame()
        self.loadingText.setText("<font color=\"green\"> Restarting Game...")
        self.loadingSubtext.setText("<font color=\"grey\"> Gimmie a Minute")
        self.loadingUptext.setText(f"<font color=\"green\"> Last Score: {self.gameCore.lastScore}")
        self.startTimer.start()


    def startGame(self):
        self.gameCore.startGame()
        self.startTimer.stop()
        self.loadingText.setText("<font color=\"red\"> Game Over")
        self.loadingSubtext.setText("<font color=\"red\"> Press R to Restart")

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(QRect(0, 0, self.gameCore.geometry().width(), self.gameCore.geometry().height()),
                       self.gameCore.background)

    def keyPressEvent(self, event: QKeyEvent):
        self.gameCore.keyEventDist(event, True)

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == 82:
            self.restartGame()
        self.gameCore.keyEventDist(event, False)


app = QApplication(sys.argv)
win = Window()
win.show()
app.exec()
