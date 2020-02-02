import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)


    def mousePressEvent(self, e):

        self.last_x = e.x()
        self.last_y = e.y()

        # painter = QtGui.QPainter(self.pixmap())
        # p = painter.pen()
        # p.setWidth(.5)
        # p.setColor(self.pen_color)
        # painter.setPen(p)
        # painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        # painter.end()
        #self.update()

        # Update the origin for next time.
        #self.last_x = e.x()
        #self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(.5)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        print(self.last_x)
        print(self.last_y)
        print(e.x)
        print(e.y)
        #painter.end()
       # self.last_x = None
      #  self.last_y = None
        self.update()

COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = Canvas()


        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()