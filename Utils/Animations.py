from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils.Resloader import resource_path
import random


class Animation:
    def __init__(self, path: str, x: int, y: int, columns: int, rows: int,  totalFrames: int, fps: int):
        super().__init__()
        self.full_pixmap = QPixmap((resource_path(path)))
        self.pos = [x, y]
        self.gridSize = [columns, rows]
        self.totalFrames = totalFrames
        self.frames = []
        self.activeFrame = 0
        self.fps = fps
        self.id = random.random()
        self.makeFrames()

    def makeFrames(self):
        jumpX = self.full_pixmap.width() / self.gridSize[0]
        jumpY = self.full_pixmap.height() / self.gridSize[1]
        print(jumpX, jumpY)
        framesLoaded = 0
        for x in range(self.gridSize[0]):
            for y in range(self.gridSize[1]):
                if framesLoaded < self.totalFrames:
                    self.frames.append(self.full_pixmap.copy(QRect(jumpX * x, jumpY * y, jumpX - 1, jumpY - 1)))
                    framesLoaded += 1


activeAnimations = []


def startAnimation(newAnimation: Animation):
    activeAnimations.append(newAnimation)
    return newAnimation.id


def stopAnimation(id: int):
    for i, x in enumerate(activeAnimations):
        if x.id == id:
            activeAnimations.pop(i)
            break


def tickAnimation():
    i = 5


def renderAnimation(pnt: QPainter):
    pnt.drawPixmap(QRect(0, 0, 64, 64), activeAnimations[0].frames[0])
    print(len(activeAnimations[0].frames))
