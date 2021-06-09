from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.Particles import ParticleSpritesheet


class PaintBtn(QPushButton):
    def __init__(self, image: str, scale, parent):
        super().__init__(parent)
        self.image = ParticleSpritesheet(image, 1, 3, 3)
        self.setGeometry(0, 0, self.image.jumpX * scale, self.image.jumpY * scale)
        print(self.image.jumpX, self.image.jumpY)
        self.scale = scale
        self.cursorPos = QPoint()

    def paintEvent(self, event):
        pnt = QPainter(self)
        self.cursorPos = QCursor().pos()
        rect = QRect(0, 0, self.width(), self.height())
        if self.isDown() or not self.isEnabled():
            pnt.drawPixmap(rect, self.image.frames[2])
        elif self.hitButton(self.mapFromGlobal(self.cursorPos)):
            pnt.drawPixmap(rect, self.image.frames[1])
        else:
            pnt.drawPixmap(rect, self.image.frames[0])
