from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.Resloader import resource_path
import random


class Asteroids:
    asteroids = []

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.texture = QPixmap(resource_path("Assets/roid.png"))
        self.width = 46
        self.height = 70
        self.speed = 5

    def tick(self, env):
        if int((random.random() * 1000) % 10) == 0:
            speed = (random.random() * 1000) % 15
            if speed < 5:
                speed = 10
            Asteroids.asteroids.append([QRect((random.random() * 1000) % 914, self.height * -1, self.width, self.height),
                                       speed])

        for aster, speed in Asteroids.asteroids:
            if env.getEarth().getSurface().intersects(QRectF(aster)):
                Asteroids.asteroids.remove([aster, speed])
            aster.setY(aster.y() + speed)
            aster.setWidth(self.width)
            aster.setHeight(self.height)

    def render(self, pnt: QPainter):
        for asteroid, speed in Asteroids.asteroids:
            pnt.drawPixmap(asteroid, self.texture)

