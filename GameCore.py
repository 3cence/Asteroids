from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from Utils.Resloader import resource_path
from Game.Player import Player
from Game.Earth import Earth
from Utils import Particles
from Game.Asteroids import Asteroids
import time


class GameCore(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setGeometry(parent.geometry())
        self.setEnabled(False)
        self.hide()

        # Asset Loading
        self.background = QPixmap(resource_path("Assets/bg.png"))

        # Game Items
        self.player = Player()
        self.earth = Earth()
        self.asteroids = Asteroids(self)

        # Score
        self.score = 0
        self.highScore = 0
        self.scoreLabel = QLabel(f"<font color=\"white\">Score: {self.score}", self)
        self.scoreLabel.setGeometry(800, 0, 160, 50)
        self.scoreLabel.setStyleSheet("background-color: #1c111a")
        font = QFont()
        font.setPointSize(20)
        font.setWeight(30)
        font.setFamily("tlwg typist")
        self.scoreLabel.setFont(font)
        self.scoreLabel.setAlignment(Qt.AlignCenter)

        # Music
        self.musicInGame = QSound(resource_path("Assets/sfx/ingame.wav"))
        self.musicInGame.setLoops(QSound.Infinite)
        self.musicOutGame = QSound(resource_path("Assets/sfx/outgame.wav"))
        self.musicOutGame.setLoops(QSound.Infinite)
        self.musicOutGame.play()

        # Tick Regulation Stuff
        self.gameRunning = False
        self.ticker = QTimer(self)
        self.ticker.setInterval(0)
        self.ticker.timeout.connect(self.tick)
        self.ticker.start()
        self.timer = QTime()
        self.timer.start()
        self.prvTime = 0
        self.prvSecondTime = 0
        self.Tps = 0.00
        self.secTps = 0
        self.targetTps = 60
        self.delay = 1.000000

    def startGame(self):
        self.show()
        self.score = 0
        QApplication.setOverrideCursor(Qt.BlankCursor)
        self.musicOutGame.stop()
        self.musicInGame.play()
        self.gameRunning = True

    def endGame(self):
        self.hide()
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        color = "red"
        self.parent.loadingText.setText("<font color=\"red\"> Game Over")
        if self.highScore < self.score:
            self.highScore = self.score
            self.parent.loadingText.setText("<font color=\"green\"> New High Score!")
            color = "green"
        self.musicOutGame.play()
        self.musicInGame.stop()
        self.parent.loadingUptext.setText(f"<font color=\"{color}\"> Score: {self.score} | High Score: {self.highScore}")
        self.gameRunning = False

    def resetGame(self):
        self.gameRunning = False

        for i in range(len(Particles.activeAnimations)):
            Particles.activeAnimations.pop(0)

        self.player = Player()
        self.asteroids = Asteroids(self)

    def paintEvent(self, event):
        pnt = QPainter(self)
        pnt.drawPixmap(QRect(0, 0, self.geometry().width(), self.geometry().height()), self.background)
        Particles.renderParticles(pnt)
        self.scoreLabel.setText(f"<font color=\"white\">Score: {self.score}")
        self.earth.render(pnt)
        self.player.render(pnt)
        self.asteroids.render(pnt)

    def tick(self):

        # Put all game-related ticking in this if
        if self.gameRunning:
            self.player.tick(self)
            self.asteroids.tick(self)
            Particles.tickParticles()

            self.repaint()

        # Tick Regulation
        self.Tps += 1.00
        self.secTps += 1
        time.sleep(self.delay / 1000)

        if time.time() - self.prvTime >= .076:
            correction = self.Tps / (self.targetTps / 12)
            self.delay *= correction
            self.Tps = 0
            self.prvTime = time.time()

        if time.time() - self.prvSecondTime >= 1:
            self.score += 1
            self.parent.setWindowTitle(f"Asteroids: {self.secTps} Tps")
            self.secTps = 0
            self.prvSecondTime = time.time()

    def getEarth(self):
        return self.earth

    def keyEventDist(self, event: QKeyEvent, isPressed: bool):
        if isPressed:
            self.player.keyDown(event)
        else:
            self.player.keyUp(event)
