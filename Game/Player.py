from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.resloader import resource_path


class Player(QRect):
    def __init__(self):
        super().__init__(100, 100, 23, 50)
        self.move = [False, False, False, False]
        self.pos = [100, 100]
        self.speed = 5
        #Load Assets
        self.texture = QPixmap(resource_path("Assets/player/player1.png"))

    def render(self, pnt: QPainter):
        pnt.drawPixmap(self, self.texture)

    def tick(self):
        if self.move[0]:
            self.pos[0] -= self.speed
        elif self.move[1]:
            self.pos[1] -= self.speed
        elif self.move[2]:
            self.pos[0] += self.speed
        elif self.move[3]:
            self.pos[1] += self.speed

        self.setX(self.pos[0])
        self.setY(self.pos[1])
        self.setWidth(23)
        self.setHeight(50)

    def keyDown(self, event: QKeyEvent):
        event = event.key()

        if event == 16777234:
            self.move[0] = True
        elif event == 16777235:
            self.move[1] = True
        elif event == 16777236:
            self.move[2] = True
        elif event == 16777237:
            self.move[3] = True

    def keyUp(self, event: QKeyEvent):
        event = event.key()

        if event == 16777234:
            self.move[0] = False
        elif event == 16777235:
            self.move[1] = False
        elif event == 16777236:
            self.move[2] = False
        elif event == 16777237:
            self.move[3] = False
