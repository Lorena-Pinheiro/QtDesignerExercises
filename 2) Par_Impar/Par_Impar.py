# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Par_Impar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelResulatdo = QtWidgets.QLabel(self.centralwidget)
        self.labelResulatdo.setGeometry(QtCore.QRect(60, 250, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResulatdo.setFont(font)
        self.labelResulatdo.setObjectName("labelResulatdo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditNumero1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumero1.setGeometry(QtCore.QRect(60, 130, 451, 31))
        self.lineEditNumero1.setObjectName("lineEditNumero1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButtonEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(220, 180, 111, 41))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 21))
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
        self.labelResulatdo.setText(_translate("MainWindow", "Resultado"))
        self.label.setText(_translate("MainWindow", "Par ou Ímpar"))
        self.label_2.setText(_translate("MainWindow", "Digite um número para saber se é par ou ímpar:"))
        self.pushButtonEnviar.setText(_translate("MainWindow", "Enviar"))