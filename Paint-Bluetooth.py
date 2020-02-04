from PyQt5.QtGui import QImage, QPainter, QIcon
from PainterUI import Ui_MainWindow
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
import serial

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.first_x, self.first_y = None, None
        self.last_x, self.last_y = None, None
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.selectedShape = None
        self.ui.actionLINE.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\diagonal-line.png'))
        self.ui.actionCIRCLE.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\dot.png'))
        self.ui.actionRECTANGLE.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\rectangle.png'))
        self.ui.actionCLEAR.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\erase.png'))
        self.ui.actionSTART.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\start.png'))
        self.ui.actionSTOP.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\stop.png'))
        # self.ui.menuCanvas.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\canvas.png'))
        # self.ui.menuPLOTTER.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\cnc.png'))
        # self.ui.menuSHAPE.setIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\shapes.png'))
        self.ui.actionCLEAR.triggered.connect(self.clear)
        self.ui.actionCIRCLE.triggered.connect(self.drawCIRCLE)
        self.ui.actionLINE.triggered.connect(self.drawLINE)
        self.ui.actionRECTANGLE.triggered.connect(self.drawRECTANGLE)
        self.ui.actionSTOP.triggered.connect(self.stop)
        self.ui.actionSTART.triggered.connect(self.start)

        # Bluetooth part
        self.s = serial.Serial('COM11', 9600, timeout=1)  # choose the outgoing one
        print("connected!")

    def mousePressEvent(self, e):
        self.first_x = e.x()
        self.first_y = e.y()

    def mouseReleaseEvent(self, e):
        painter = QtGui.QPainter(self.image)
        p = painter.pen()
        painter.setPen(p)
        self.last_x = e.x()
        self.last_y = e.y()

        if self.selectedShape == "LINE":
            painter.drawLine(self.first_x, self.first_y, self.last_x, self.last_y)
            self.first_x = str(self.first_x)
            self.first_y = str(self.first_y)
            self.last_x = str(self.last_x)
            self.last_y = str(self.last_y)
            self.s.write(
                bytes("/" + "L" + "," + self.first_x + "," + self.first_y + "," + self.last_x + "," + self.last_y , 'UTF-8'))

        if self.selectedShape == "RECTANGLE":
            w = self.last_x - self.first_x
            h = self.last_y - self.first_y
            painter.drawRect(self.first_x, self.first_y, w, h)
            self.first_x = str(self.first_x)
            self.first_y = str(self.first_y)
            w = str(w)
            h = str(h)
            self.s.write(bytes("/" + "R" + "," + self.first_x + "," + self.first_y + "," + w + "," + h , 'UTF-8'))

        if self.selectedShape == "CIRCLE":
            w = self.last_x - self.first_x
            h = self.last_y - self.first_y
            painter.drawEllipse(self.first_x, self.first_y, h, h)
            self.first_x = str(self.first_x)
            self.first_y = str(self.first_y)
            h = str(h)
            self.s.write(bytes("/" + "C" + "," + self.first_x + "," + self.first_y + "," + h + "," + h , 'UTF-8'))

        print(self.first_x)
        print(self.first_y)
        print(self.last_x)
        print(self.last_y)
        self.update()

    def clear(self):
        print("clear")
        self.image.fill(Qt.white)
        self.update()
        self.ui.actionSTART.setText("START")

    def stop(self):
        print("stop")
        self.s.write(bytes("off", 'UTF-8'))

    def start(self):
        self.ui.actionSTART.setText("RESUME")
        print("start")
        self.s.write(bytes("on", 'UTF-8'))



    def drawRECTANGLE(self):
        self.selectedShape = "RECTANGLE"

    def drawLINE(self):
        self.selectedShape = "LINE"

    def drawCIRCLE(self):
        self.selectedShape = "CIRCLE"

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.setStyleSheet("""
                QMenuBar {
                    background-color: rgb(102,0,102);
                    color: rgb(255,255,255);
                    border: 1px solid #000;
                }

                QMenuBar::item:selected {
                     border-color: darkblue;
                    background: rgba(153, 0, 153, 150);
                }
                QMenu::item:selected {
                     border-color: darkblue;
                    background: rgba(153, 0, 153, 150);
                }

             """)
    application.setWindowIcon(QIcon(r'C:\Users\Gamila\Documents\GitHub\CNC-Plotter\Icons\canvas.png'))
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
