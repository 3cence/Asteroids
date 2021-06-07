from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils.Resloader import resource_path
import random


class Animation:
    def __init__(self, path: str, x: int, y: int, columns: int, rows: int, totalFrames: int, fps: int, scale=1.00, loops=False):
        super().__init__()
        self.full_pixmap = QPixmap((resource_path(path)))
        self.pos = [x, y]
        self.gridSize = [columns, rows]
        self.totalFrames = totalFrames
        self.scale = scale
        self.loops = loops
        self.jumpX = int(self.full_pixmap.width() / self.gridSize[0])
        self.jumpY = int(self.full_pixmap.height() / self.gridSize[1])
        self.frames = []
        self.activeFrame = 0
        self.ticksSinceLastFrame = 0
        self.fps = fps
        self.id = -1
        self.makeFrames()

    def makeFrames(self):
        print(self.jumpX, self.jumpY)
        framesLoaded = 0
        for y in range(self.gridSize[1]):
            for x in range(self.gridSize[0]):
                if framesLoaded < self.totalFrames:
                    self.frames.append(self.full_pixmap.copy(QRect(self.jumpX * x, self.jumpY * y, self.jumpX - 1, self.jumpY - 1)))
                    framesLoaded += 1


activeAnimations = []


def startAnimation(newAnimation: Animation):
    newAnimation.id = random.random()
    activeAnimations.append(newAnimation)
    return newAnimation.id


def stopAnimation(id: int):
    for i, x in enumerate(activeAnimations):
        if x.id == id:
            activeAnimations.pop(i)
            break


def tickAnimation():
    toRemove = []
    for i, animation in enumerate(activeAnimations):
        if animation.ticksSinceLastFrame >= 60 / animation.fps:
            animation.activeFrame += 1
            animation.ticksSinceLastFrame = 0
        else:
            animation.ticksSinceLastFrame += 1

        if animation.activeFrame >= animation.totalFrames:
            if not animation.loops:
                toRemove.append(animation)
            else:
                animation.activeFrame = 0
    for candidates in toRemove:
        activeAnimations.remove(candidates)


def renderAnimation(pnt: QPainter):
    for animation in activeAnimations:
        pnt.drawPixmap(QRect(animation.pos[0], animation.pos[1], animation.jumpX * animation.scale,
                             animation.jumpY * animation.scale),
                       animation.frames[animation.activeFrame])
    # pnt.drawPixmap(QRect(0, 0, 64, 64), activeAnimations[0].frames[0])
    # print(activeAnimations[0].activeFrame)
