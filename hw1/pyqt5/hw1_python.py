# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Özge/PycharmProjects/pythonProject12/hw1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1262, 747)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/654094baad0b8073efbda63734a85b45.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#centralwidget{\n"
"background-image: url(:/icons/654094baad0b8073efbda63734a85b45.jpg);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("#centralwidget\n"
"{\n"
"background-image: url(:/icons/20354345.jpg);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 161, 31))
        self.pushButton.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(22, 49, 136, 255), stop:0.225 rgba(41, 71, 166, 255), stop:0.285 rgba(74, 155, 204, 255), stop:0.345 rgba(102, 145, 235, 255), stop:0.415 rgba(112, 138, 245, 255), stop:0.460227 rgba(96, 185, 230, 255), stop:0.52 rgba(76, 130, 209, 255), stop:0.57 rgba(51, 153, 187, 255), stop:0.635 rgba(42, 77, 168, 255), stop:0.695 rgba(68, 123, 202, 255), stop:0.75 rgba(86, 112, 218, 255), stop:0.815 rgba(73, 168, 208, 255), stop:0.88 rgba(51, 89, 187, 255), stop:0.935 rgba(26, 43, 137, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 901, 461))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 180, 151, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 85, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 80, 601, 461))
        self.label_3.setStyleSheet("background-image: url(:/icons/Brain-inspiredAI-600x400.jpeg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(210, 70, 22, 51))
        self.verticalSlider.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(22, 49, 136, 255), stop:0.225 rgba(41, 71, 166, 255), stop:0.285 rgba(74, 155, 204, 255), stop:0.345 rgba(102, 145, 235, 255), stop:0.415 rgba(112, 138, 245, 255), stop:0.460227 rgba(96, 185, 230, 255), stop:0.52 rgba(76, 130, 209, 255), stop:0.57 rgba(51, 153, 187, 255), stop:0.635 rgba(42, 77, 168, 255), stop:0.695 rgba(68, 123, 202, 255), stop:0.75 rgba(86, 112, 218, 255), stop:0.815 rgba(73, 168, 208, 255), stop:0.88 rgba(51, 89, 187, 255), stop:0.935 rgba(26, 43, 137, 255), stop:1 rgba(35, 40, 3, 255));")
        self.verticalSlider.setMaximum(1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 161, 61))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(290, 0, 601, 61))
        self.frame_2.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 601, 61))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 130, 61, 16))
        self.label_6.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 40, 61, 16))
        self.label_7.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 190, 41, 41))
        self.label_2.setStyleSheet("border-image: url(:/icons/Bokehlicia-Captiva-Preferences-color.ico);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 190, 31, 31))
        self.label_8.setStyleSheet("border-image: url(:/icons/Hopstarter-Soft-Scraps-Button-Blank-Gray.ico);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 270, 261, 441))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background-color: rgb(0, 85, 127);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 90, 241, 22))
        self.horizontalSlider.setMaximum(15)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 150, 241, 22))
        self.horizontalSlider_2.setMaximum(15)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 210, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(22, 49, 136, 255), stop:0.225 rgba(41, 71, 166, 255), stop:0.285 rgba(74, 155, 204, 255), stop:0.345 rgba(102, 145, 235, 255), stop:0.415 rgba(112, 138, 245, 255), stop:0.460227 rgba(96, 185, 230, 255), stop:0.52 rgba(76, 130, 209, 255), stop:0.57 rgba(51, 153, 187, 255), stop:0.635 rgba(42, 77, 168, 255), stop:0.695 rgba(68, 123, 202, 255), stop:0.75 rgba(86, 112, 218, 255), stop:0.815 rgba(73, 168, 208, 255), stop:0.88 rgba(51, 89, 187, 255), stop:0.935 rgba(26, 43, 137, 255), stop:1 rgba(35, 40, 3, 255));\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dial = QtWidgets.QDial(self.frame_3)
        self.dial.setGeometry(QtCore.QRect(80, 290, 101, 101))
        self.dial.setMaximum(2)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1262, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Enter Image"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Halime Özge KABAK </p><p>      180403001</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">IMAGE PROCESSING HW1</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Invisible</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Visible</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Blur The Image"))

import icons_rc
