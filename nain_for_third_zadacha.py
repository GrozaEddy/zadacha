import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.x = self.y = self.r = 0import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = self.y = self.r = 0
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.r = choice(list(range(50, 300)))
        self.x, self.y = choice(list(range(50, 550))), choice(list(range(50, 550)))
        self.paintEvent(self.event)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        r, g, b = choice(list(range(0, 256))), choice(list(range(0, 256))), choice(
            list(range(0, 256)))
        qp.setBrush(r, g, b)
        qp.drawEllipse(self.x, self.y, self.r, self.r)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.r = choice(list(range(50, 300)))
        self.x, self.y = choice(list(range(50, 550))), choice(list(range(50, 550)))
        self.paintEvent(self.event)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        r, g, b = choice(list(range(0, 255))), choice(list(range(0, 255))), choice(
            list(range(0, 255)))
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(self.x, self.y, self.r, self.r)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
