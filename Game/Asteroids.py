from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from Utils.Resloader import resource_path
from Utils import Particles
import random


class Asteroids:
    asteroids = []

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.texture = QPixmap(resource_path("Assets/roid.png"))
        self.width = 46
        self.height = 70
        self.speed = 5

        for i in range(len(Asteroids.asteroids)):
            Asteroids.asteroids.pop(0)

        # Sfx
        self.sfxImpact = resource_path("Assets/sfx/small_crash.wav")

        # Particles
        self.boom = Particles.Particle("Assets/spritesheets/explosion.png", columns=4, rows=4,
                                       totalFrames=16, fps=50)
        self.trail = Particles.Particle("Assets/spritesheets/trailing_fire.png", columns=3, rows=3,
                                        totalFrames=8, fps=20)

    def tick(self, env):
        # Spawn new asteroid
        if int((random.random() * 1000) % 10) == 0:
            speed = ((random.random() * 1000) % 10) + 6
            Asteroids.asteroids.append([QRect(int(random.random() * 1000) % 914, self.height * -1, self.width, self.height),
                                       speed])

        for aster, speed in Asteroids.asteroids:
            # Destroy asteroid on impact with earth
            if env.getEarth().getSurface().intersects(QRectF(aster)):
                Particles.spawnParticle(self.boom, aster.x(), aster.y() + 20)
                QSound.play(self.sfxImpact)
                Asteroids.asteroids.remove([aster, speed])

            # Spawn Trail
            if int((random.random() * 1000) % 5) == 0:
                trailScale = 2
                Particles.spawnParticle(self.trail, aster.x() + ((aster.width() / 2) - (self.trail.jumpX * trailScale) / 2),
                                        aster.y(), trailScale)

            # Update Position
            aster.setY(aster.y() + speed)
            aster.setWidth(self.width)
            aster.setHeight(self.height)

    def render(self, pnt: QPainter):
        for asteroid, speed in Asteroids.asteroids:
            pnt.drawPixmap(asteroid, self.texture)

