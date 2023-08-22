from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPainter, QPen
from PyQt5.QtCore import QTimer, QTime, Qt

app = QApplication([])


class ClockApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)  # 去掉窗口边框
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 始终置顶
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QLabel(self)
        self.central_widget.setGeometry(10, 10, 280, 130)
        self.central_widget.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.central_widget.setFont(font)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # 拖动相关变量
        self.draggable = False
        self.offset = None

    def update_time(self):
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("hh:mm:ss")
        self.central_widget.setText(formatted_time)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.yellow)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(5, 5, 290, 140)  # 绘制黄色的边框

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable and self.offset:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            self.offset = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()


clock_app = ClockApp()
clock_app.show()
app.exec_()
