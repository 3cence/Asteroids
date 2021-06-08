from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from QtOverrides.PaintBtn import *
from Utils.Resloader import resource_path


class LoadingScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print("Loading the start screen")
        self.setGeometry(parent.geometry())

        self.startBtn = PaintBtn(resource_path("Assets/play.png"), self)

        #Load Stuff
        self.title = QPixmap(resource_path("Assets/title.png"))

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.setBrush(Qt.blue)
        pnt.drawPixmap(self.geometry(), self.parent.gameCore.background)
        pnt.drawPixmap(QRect(20, 0, self.title.width(), self.title.height()), self.title)
