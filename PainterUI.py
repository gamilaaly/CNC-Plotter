# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PainterUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setObjectName("menubar")
        self.menuCanvas = QtWidgets.QMenu(self.menubar)
        self.menuCanvas.setObjectName("menuCanvas")
        self.menuSHAPE = QtWidgets.QMenu(self.menubar)
        self.menuSHAPE.setObjectName("menuSHAPE")
        self.menuPLOTTER = QtWidgets.QMenu(self.menubar)
        self.menuPLOTTER.setObjectName("menuPLOTTER")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCLEAR = QtWidgets.QAction(MainWindow)
        self.actionCLEAR.setObjectName("actionCLEAR")
        self.actionLINE = QtWidgets.QAction(MainWindow)
        self.actionLINE.setObjectName("actionLINE")
        self.actionRECTANGLE = QtWidgets.QAction(MainWindow)
        self.actionRECTANGLE.setObjectName("actionRECTANGLE")
        self.actionCIRCLE = QtWidgets.QAction(MainWindow)
        self.actionCIRCLE.setObjectName("actionCIRCLE")
        self.actionSTART = QtWidgets.QAction(MainWindow)
        self.actionSTART.setObjectName("actionSTART")
        self.actionSTOP = QtWidgets.QAction(MainWindow)
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
