from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.resloader import resource_path


class Earth(QRect):
    def __init__(self):
        super().__init__(0, 400, 800, 100)
        self.surface = QPainterPath()

        self.prepareSurface()
        #Load Assets
        self.texture = QPixmap(resource_path("Assets/earth.png"))

    def prepareSurface(self):
        self.surface.moveTo(0, 400)
        self.surface.lineTo(400, 300)
        self.surface.lineTo(800, 400)

    def getSurface(self):
        return self.surface

    def render(self, pnt: QPainter):
        pnt.drawPixmap(self, self.texture)
        pnt.setPen(Qt.cyan)
        pnt.drawPath(self.surface)
