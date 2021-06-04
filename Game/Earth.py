from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.resloader import resource_path


class Earth(QRect):
    def __init__(self):
        super().__init__(0, 500, 960, 100)
        self.surface = QPainterPath()

        self.prepareSurface()
        #Load Assets
        self.texture = QPixmap(resource_path("Assets/earth.png"))

    def prepareSurface(self):
        offset = 500
        self.surface.moveTo(900, 100 + offset)
        self.surface.lineTo(0, 32 + offset)
        self.surface.lineTo(37, 26 + offset)
        self.surface.lineTo(66, 15 + offset)
        self.surface.lineTo(78, 16 + offset)
        self.surface.lineTo(109, 2 + offset)
        self.surface.lineTo(164, 2 + offset)
        self.surface.lineTo(203, 15 + offset)
        self.surface.lineTo(320, 29 + offset)
        self.surface.lineTo(354, 24 + offset)
        self.surface.lineTo(419, 25 + offset)
        self.surface.lineTo(559, 33 + offset)
        self.surface.lineTo(595, 34 + offset)
        self.surface.lineTo(616, 23 + offset)
        self.surface.lineTo(647, 24 + offset)
        self.surface.lineTo(720, 34 + offset)
        self.surface.lineTo(834, 39 + offset)
        self.surface.lineTo(911, 35 + offset)
        self.surface.lineTo(952, 13 + offset)
        self.surface.lineTo(959, 12 + offset)

    def getSurface(self):
        return self.surface

    def render(self, pnt: QPainter):
        pnt.drawPixmap(self, self.texture)
        pnt.setPen(Qt.cyan)
        pnt.setBrush(Qt.blue)
        # pnt.drawPath(self.surface)
