# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fibonnaci.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lineEditNumero1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumero1.setGeometry(QtCore.QRect(120, 180, 551, 41))
        self.lineEditNumero1.setObjectName("lineEditNumero1")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(120, 240, 551, 191))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelResultado.setFont(font)
        self.labelResultado.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelResultado.setWordWrap(True)
        self.labelResultado.setObjectName("labelResultado")
        self.pushButtonEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(340, 470, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonEnviar.setFont(font)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
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
        self.label.setText(_translate("MainWindow", "Fibonnaci"))
        self.label_2.setText(_translate("MainWindow", "Digite a quantidade de números a ser exibidos da sequencia de fibonnaci:"))
        self.labelResultado.setText(_translate("MainWindow", "Resultado:"))
        self.pushButtonEnviar.setText(_translate("MainWindow", "Enviar"))
