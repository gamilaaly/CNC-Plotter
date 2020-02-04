# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PainterUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/paint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuCanvas = QtWidgets.QMenu(self.menubar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/canvas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCanvas.setIcon(icon1)
        self.menuCanvas.setObjectName("menuCanvas")
        self.menuSHAPE = QtWidgets.QMenu(self.menubar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/shapes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSHAPE.setIcon(icon2)
        self.menuSHAPE.setObjectName("menuSHAPE")
        self.menuPLOTTER = QtWidgets.QMenu(self.menubar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/cnc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPLOTTER.setIcon(icon3)
        self.menuPLOTTER.setObjectName("menuPLOTTER")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCLEAR = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCLEAR.setIcon(icon4)
        self.actionCLEAR.setObjectName("actionCLEAR")
        self.actionLINE = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/diagonal-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLINE.setIcon(icon5)
        self.actionLINE.setObjectName("actionLINE")
        self.actionRECTANGLE = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRECTANGLE.setIcon(icon6)
        self.actionRECTANGLE.setObjectName("actionRECTANGLE")
        self.actionCIRCLE = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCIRCLE.setIcon(icon7)
        self.actionCIRCLE.setObjectName("actionCIRCLE")
        self.actionSTART = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSTART.setIcon(icon8)
        self.actionSTART.setObjectName("actionSTART")
        self.actionSTOP = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSTOP.setIcon(icon9)
        self.actionSTOP.setObjectName("actionSTOP")
        self.menuCanvas.addAction(self.actionCLEAR)
        self.menuSHAPE.addAction(self.actionLINE)
        self.menuSHAPE.addAction(self.actionRECTANGLE)
        self.menuSHAPE.addAction(self.actionCIRCLE)
        self.menuPLOTTER.addAction(self.actionSTART)
        self.menuPLOTTER.addAction(self.actionSTOP)
        self.menubar.addAction(self.menuCanvas.menuAction())
        self.menubar.addAction(self.menuSHAPE.menuAction())
        self.menubar.addAction(self.menuPLOTTER.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint Application"))
        self.menuCanvas.setTitle(_translate("MainWindow", "CANVAS"))
        self.menuSHAPE.setTitle(_translate("MainWindow", "SHAPE"))
        self.menuPLOTTER.setTitle(_translate("MainWindow", "PLOTTER"))
        self.actionCLEAR.setText(_translate("MainWindow", "CLEAR"))
        self.actionLINE.setText(_translate("MainWindow", "LINE"))
        self.actionRECTANGLE.setText(_translate("MainWindow", "RECTANGLE"))
        self.actionCIRCLE.setText(_translate("MainWindow", "CIRCLE"))
        self.actionSTART.setText(_translate("MainWindow", "START"))
        self.actionSTOP.setText(_translate("MainWindow", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
