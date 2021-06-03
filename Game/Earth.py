from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.resloader import resource_path


class Earth(QRect):
    def __init__(self):
        super().__init__(0, 400, 800, 100)

        #Load Assets
        self.texture = QPixmap(resource_path("Assets/earth.png"))

    def render(self, pnt: QPainter):
        pnt.drawPixmap(self, self.texture)
