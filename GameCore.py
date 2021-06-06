from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.Resloader import resource_path
from Game.Player import Player
from Game.Earth import Earth
from Utils import Animations
import time


class GameCore(QWidget):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.mainWindow = mainWindow
        self.setGeometry(mainWindow.geometry())
        self.setEnabled(False)

        #Asset Loading
        self.background = QPixmap(resource_path("Assets/bg.png"))

        #Game Items
        self.player = Player()
        self.earth = Earth()

        #Tick Regulation Stuff
        self.timer = QTime()
        self.timer.start()
        self.prvTime = 0
        self.prvSecondTime = 0
        self.Tps = 0.00
        self.secTps = 0
        self.targetTps = 50
        self.delay = 1.000000

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(QRect(0, 0, self.geometry().width(), self.geometry().height()), self.background)
        self.earth.render(pnt)
        self.player.render(pnt)

    def tick(self):
        self.player.tick(self)

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
            print(self.secTps)
            self.secTps = 0
            self.prvSecondTime = time.time()

    def getEarth(self):
        return self.earth

    def keyEventDist(self, event: QKeyEvent, isPressed: bool):
        if isPressed:
            self.player.keyDown(event)
        else:
            self.player.keyUp(event)
