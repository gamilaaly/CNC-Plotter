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
        MainWindow.resize(800, 345)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rectangleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rectangleBtn.setGeometry(QtCore.QRect(20, 140, 89, 25))
        self.rectangleBtn.setObjectName("rectangleBtn")
        self.lineBtn = QtWidgets.QPushButton(self.centralwidget)
        self.lineBtn.setGeometry(QtCore.QRect(20, 190, 89, 25))
        self.lineBtn.setObjectName("lineBtn")
        self.circlrBtn = QtWidgets.QPushButton(self.centralwidget)
        self.circlrBtn.setGeometry(QtCore.QRect(20, 240, 89, 25))
        self.circlrBtn.setObjectName("circlrBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(20, 90, 89, 25))
        self.stopBtn.setObjectName("stopBtn")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 40, 89, 25))
        self.startBtn.setObjectName("startBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(126, 16, 651, 251))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rectangleBtn.setText(_translate("MainWindow", "Rectangle"))
        self.lineBtn.setText(_translate("MainWindow", "Line"))
        self.circlrBtn.setText(_translate("MainWindow", "Circle"))
        self.stopBtn.setText(_translate("MainWindow", "STOP"))
        self.startBtn.setText(_translate("MainWindow", "START"))
