from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.Particles import ParticleSpritesheet
import time


class PaintBtn(QPushButton):
    def __init__(self, image: str, columns: int, rows: int, frames: int, parent):
        super().__init__(parent)
        self.image = ParticleSpritesheet(image, columns, rows, frames)
        self.setGeometry(0, 0, self.image.jumpX, self.image.jumpY)
        self.cursorPos = QPoint()
        self.clickCooldown = 0

    def paintEvent(self, event):
        pnt = QPainter(self)
        self.cursorPos = QCursor().pos()
        if self.isDown():
            pnt.drawPixmap(self.geometry(), self.image.frames[2])
        elif self.hitButton(self.mapFromGlobal(self.cursorPos)):
            pnt.drawPixmap(self.geometry(), self.image.frames[1])
        else:
            pnt.drawPixmap(self.geometry(), self.image.frames[0])
