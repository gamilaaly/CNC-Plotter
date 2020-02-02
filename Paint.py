from PainterUI import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.first_x, self.first_y = None, None
        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#81588d')
        self.painter,self.p = None, None
        self.pixmap = QtGui.QPixmap(700, 400)
        self.ui.label.setPixmap(self.pixmap)

    def mousePressEvent(self, e):
        self.first_x = e.x()
        self.first_y = e.y()

    def mouseReleaseEvent(self, e):
        self.painter = QtGui.QPainter(self.pixmap)
        self.p = self.painter.pen()
        self.painter.setPen(self.p)
        self.p.setWidth(4)
        self.p.setColor(self.pen_color)
        self.last_x = e.x()
        self.last_y = e.y()
        self.painter.drawLine(self.first_x, self.first_y, self.last_x, self.last_y)
        print(self.first_x)
        print(self.first_y)
        print(self.last_x)
        print(self.last_y)
        self.ui.label.update()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
