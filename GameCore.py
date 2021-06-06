from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.Resloader import resource_path
from Game.Player import Player
from Game.Earth import Earth
from Utils import Animations
from Game.Asteroids import Asteroids
import time


class GameCore(QWidget):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.mainWindow = mainWindow
        self.setGeometry(mainWindow.geometry())
        self.setEnabled(False)
        self.hide()

        #Asset Loading
        self.background = QPixmap(resource_path("Assets/bg.png"))
        self.testAnimation = Animations.Animation("Assets/spritesheets/test_anim.gif", 100, 100, 4, 3, 10, 10)

        #Game Items
        self.player = Player()
        self.earth = Earth()
        self.asteroids = Asteroids(self)

        #Tick Regulation Stuff
        self.ticker = QTimer(self)
        self.ticker.setInterval(0)
        self.ticker.timeout.connect(self.tick)
        self.ticker.start()

        self.gameRunning = False

        self.timer = QTime()
        self.timer.start()
        self.prvTime = 0
        self.prvSecondTime = 0
        self.Tps = 0.00
        self.secTps = 0
        self.targetTps = 50
        self.delay = 1.000000

    def startGame(self):
        self.show()
        self.gameRunning = True


    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(QRect(0, 0, self.geometry().width(), self.geometry().height()), self.background)
        # Animations.renderAnimation(pnt)
        self.earth.render(pnt)
        self.player.render(pnt)
        self.asteroids.render(pnt)

    def tick(self):

        #Put all game-related ticking in this If
        if self.gameRunning:
            self.player.tick(self)
            self.asteroids.tick(self)
            # Animations.tickAnimation()

            self.repaint()

        #Tick Regulation
        self.Tps += 1.00
        self.secTps += 1
        time.sleep(self.delay / 1000)

        if time.time() - self.prvTime >= .076:
            correction = self.Tps / (self.targetTps / 12)
            self.delay *= correction
            self.Tps = 0
            self.prvTime = time.time()

        if time.time() - self.prvSecondTime >= 1:
            self.mainWindow.setWindowTitle(f"Asteroids: {self.secTps} Tps")
            self.secTps = 0
            self.prvSecondTime = time.time()

    def getEarth(self):
        return self.earth

    def keyEventDist(self, event: QKeyEvent, isPressed: bool):
        if isPressed:
            self.player.keyDown(event)
        else:
            self.player.keyUp(event)
