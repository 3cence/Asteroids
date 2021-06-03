from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.resloader import resource_path
import time


class Player:
    def __init__(self):
        super().__init__()
        self.texture = QPixmap(resource_path("Assets/player/player1.png"))
        self.hitbox = QRect(100, 100, 21, 50)

    def render(self, pnt: QPainter):
        pnt.drawPixmap(self.hitbox, self.texture)

    def tick(self):
        x = 1
