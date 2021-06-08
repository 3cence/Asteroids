from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from Utils import Particles
import time

from Utils.Resloader import resource_path


class Player(QRect):
    def __init__(self):
        super().__init__(128, 452, 23, 50)
        self.move = [False, False, False, False]
        self.pos = [100, 100]
        self.speed = 4
        self.health = 3

        #iFrames in seconds
        self.lastInvincible = 0
        self.iFrames = 1
        self.onIFrames = False
        self.ticksSinceHit = 0

        #Load Assets
        self.activeTexture = 0
        self.texture = [QPixmap(resource_path("Assets/player/player1.png")),
                        QPixmap(resource_path("Assets/player/player2.png")),
                        QPixmap(resource_path("Assets/player/player3.png"))]
        self.heart = QPixmap(resource_path("Assets/player/heart.png"))

    def render(self, pnt: QPainter):
        if self.ticksSinceHit % 2 == 0 and self.health != 0:
            pnt.drawPixmap(self, self.texture[self.activeTexture])

        for i in range(self.health):
            pnt.drawPixmap(QRect(self.heart.width() * i + 4 * i, 0,
                                 self.heart.width(), self.heart.height()), self.heart)

    def tick(self, env):
        surface = env.getEarth().getSurface()
        if time.time() - self.lastInvincible >= self.iFrames:
            self.onIFrames = False
        else:
            self.onIFrames = True
        self.pos = [self.x(), self.y()]

        # Move the player
        self.pos[1] += self.speed

        if self.move[0]:
            self.pos[0] -= self.speed
        elif self.move[2]:
            self.pos[0] += self.speed

        # Don't fall through the earth!!
        while surface.intersects(QRectF(self.pos[0], self.pos[1], self.width(), self.height())):
            self.pos[1] -= 1
        self.pos[1] += 1

        # Protect from leaving the screen
        if not self.pos[0] < 0 and not self.pos[0] > 938:
            self.setX(self.pos[0])
            self.setY(self.pos[1])
            self.setWidth(23)
            self.setHeight(50)

        #Do i get hit by an asteroid? (And invince frames)
        if not self.onIFrames:
            self.ticksSinceHit = 0
            for asteroid, speed in env.asteroids.asteroids:
                if self.intersects(asteroid):
                    if self.activeTexture < 2:
                        self.activeTexture += 1
                    Particles.spawnParticle(env.asteroids.boom, self.pos[0] - 90, self.pos[1] - 60, 4)
                    QSound.play(resource_path("Assets/sfx/crash.wav"))
                    self.health -= 1
                    self.ticksSinceHit = 0
                    self.lastInvincible = time.time()
        else:
            self.ticksSinceHit += 1

        #DID YOU DIE BOX
        if self.health == 0 and self.ticksSinceHit == 30:
            env.endGame()


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

    def getRectF(self):
        return QRectF(self.x(), self.y(), self.width(), self.height())
