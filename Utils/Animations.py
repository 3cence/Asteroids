from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Utils.Resloader import resource_path


class Animation:
    def __init__(self, path: str, columns: int, rows: int, fps: int):
        super().__init__()
        self.full_pixmap = QPixmap((resource_path(path)))


activeAnimations = []


def tickAnimation():
    print("Ticking Animation")


def renderAnimation():
    print("Rendering Animation")
