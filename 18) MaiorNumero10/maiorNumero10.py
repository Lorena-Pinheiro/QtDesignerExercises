# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maiorNumero10.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonMostrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMostrar.setGeometry(QtCore.QRect(460, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonMostrar.setFont(font)
        self.pushButtonMostrar.setObjectName("pushButtonMostrar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(140, 200, 521, 211))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelResultado.setFont(font)
        self.labelResultado.setText("")
        self.labelResultado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResultado.setWordWrap(True)
        self.labelResultado.setObjectName("labelResultado")
        self.lineEditNumero1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumero1.setGeometry(QtCore.QRect(140, 90, 291, 41))
        self.lineEditNumero1.setObjectName("lineEditNumero1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButtonMostrar.setText(_translate("MainWindow", "Enviar"))
        self.pushButtonMostrar.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Informe 10 números para saber qual é maior:"))
