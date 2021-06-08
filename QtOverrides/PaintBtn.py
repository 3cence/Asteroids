from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.Particles import ParticleSpritesheet


class PaintBtn(QPushButton):
    def __init__(self, image: str, parent):
        super().__init__(parent)
        self.image = ParticleSpritesheet(image, 1, 3, 3)
        self.setGeometry(0, 0, self.image.jumpX, self.image.jumpY)

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(self.geometry(), self.image.frames[0])
