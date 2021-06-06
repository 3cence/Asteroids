from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils.Resloader import resource_path
import random


class Animation:
    def __init__(self, path: str, x: int, y: int, columns: int, rows: int,  totalFrames: int, fps: int):
        super().__init__()
        self.full_pixmap = QPixmap((resource_path(path)))
        self.pos = [x, y]
        self.size = [columns, rows]
        self.totalFrames = totalFrames
        self.frames = []
        self.activeFrame = 0
        self.fps = fps
        self.id = random.random()
    #     self.makeFrames()
    #
    # def makeFrames(self):
    #     self.frames[0] = QPainter_PixmapFragment.create(0, 0, QRect(0, 0, 10, 10))


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
    print(activeAnimations)


def renderAnimation(pnt: QPainter):
    pnt.drawPixmap(activeAnimations[0].full_pixmap.rect(), activeAnimations[0].full_pixmap)
