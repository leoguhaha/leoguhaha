import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QSizePolicy
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import random


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        red_balls = random.sample(range(1, 34), 6)
        red_balls.sort()

        blue_ball = [random.randint(1, 16)]

        self.title = '双色球必中！'
        self.initUI(red_balls + blue_ball)

    def initUI(self, list):
        self.setWindowTitle(self.title)

        self.setGeometry(600, 300, 350, 70)
        self.setMinimumSize(350, 70)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QHBoxLayout()

        label_red = QLabel(' '.join(map(str, list[:6])), self)
        label_red.setFont(QFont('Times New Roman', 18, QFont.Bold))
        label_red.setStyleSheet(f"color: red; border-radius: 30px; padding: 10px; border: 2px solid red;")
        # increase the size policy of red balls label to get more space
        label_red.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        label_blue = QLabel(str(list[-1]), self)
        label_blue.setFont(QFont('Times New Roman', 18, QFont.Bold))
        label_blue.setStyleSheet(f"color: blue; border-radius: 30px; padding: 10px; border: 2px solid blue;")

        layout.setSpacing(16)

        layout.addWidget(label_red)
        layout.addWidget(label_blue)

        widget.setLayout(layout)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor('#F2F2F2'))
        self.setPalette(palette)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MyApp()

    sys.exit(app.exec_())
