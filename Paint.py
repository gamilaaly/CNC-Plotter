from PyQt5.QtGui import QImage, QPainter, QIcon
from PainterUI import Ui_MainWindow
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {'databaseURL': 'https://cnc-plotter-17855.firebaseio.com/'})
control = db.reference()


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QIcon('Icons/paint.png'))
        self.ui.setupUi(self)
        self.first_x, self.first_y = None, None
        self.last_x, self.last_y = None, None
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.selectedShape = None
        self.ui.actionLINE.setIcon(QIcon('Icons/diagonal-line.png'))
        self.ui.actionCIRCLE.setIcon(QIcon('Icons/dot.png'))
        self.ui.actionRECTANGLE.setIcon(QIcon('Icons/rectangle.png'))
        self.ui.actionCLEAR.setIcon(QIcon('Icons/erase.png'))
        self.ui.actionSTART.setIcon(QIcon('Icons/start.png'))
        self.ui.actionSTOP.setIcon(QIcon('Icons/stop.png'))
        self.ui.actionCLEAR.triggered.connect(self.clear)
        self.ui.actionCIRCLE.triggered.connect(self.drawCIRCLE)
        self.ui.actionLINE.triggered.connect(self.drawLINE)
        self.ui.actionRECTANGLE.triggered.connect(self.drawRECTANGLE)
        self.ui.actionSTOP.triggered.connect(self.stop)
        self.ui.actionSTART.triggered.connect(self.start)


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
            control.update({'control/parameters/p1/p11': self.first_x})
            control.update({'control/parameters/p1/p12': self.first_y})
            control.update({'control/parameters/p2/p21': self.last_x})
            control.update({'control/parameters/p2/p22': self.last_y})

        if self.selectedShape == "RECTANGLE":
            w = self.last_x - self.first_x
            h = self.last_y - self.first_y
            painter.drawRect(self.first_x, self.first_y, w, h)
            control.update({'control/parameters/p1/p11': self.first_x})
            control.update({'control/parameters/p1/p12': self.first_y})
            control.update({'control/parameters/p2/p21': h})
            control.update({'control/parameters/p2/p22': w})

        if self.selectedShape == "CIRCLE":
            w = self.last_x - self.first_x
            h = self.last_y - self.first_y
            painter.drawEllipse(self.first_x, self.first_y, h, h)
            control.update({'control/parameters/p1/p11': self.first_x})
            control.update({'control/parameters/p1/p12': self.first_y})
            control.update({'control/parameters/p2/p21': h})
            control.update({'control/parameters/p2/p22': h})

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
        control.update({'control/on': 0})
        print("stop")

    def start(self):
        control.update({'control/on': 1})
        self.ui.actionSTART.setText("RESUME")
        print("start")

    def drawRECTANGLE(self):
        control.update({'control/shape': "R"})
        self.selectedShape = "RECTANGLE"

    def drawLINE(self):
        self.selectedShape = "LINE"
        control.update({'control/shape': "L"})

    def drawCIRCLE(self):
        self.selectedShape = "CIRCLE"
        control.update({'control/shape': "C"})

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
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
