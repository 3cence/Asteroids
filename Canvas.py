from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.resloader import resource_path
from Game.Player import Player
from Game.Earth import Earth
import time


class Canvas(QWidget):
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
        self.delay = 1

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(QRect(0, 0, self.geometry().width(), self.geometry().height()), self.background)
        self.player.render(pnt)
        self.earth.render(pnt)

    def tick(self):
        self.player.tick()
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