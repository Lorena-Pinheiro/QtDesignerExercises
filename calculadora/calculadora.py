# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 665)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 481, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(10, 150, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.seteButton = QtWidgets.QPushButton(self.centralwidget)
        self.seteButton.setGeometry(QtCore.QRect(10, 240, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.seteButton.setFont(font)
        self.seteButton.setObjectName("seteButton")
        self.quatroButton = QtWidgets.QPushButton(self.centralwidget)
        self.quatroButton.setGeometry(QtCore.QRect(10, 330, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.quatroButton.setFont(font)
        self.quatroButton.setObjectName("quatroButton")
        self.umButton = QtWidgets.QPushButton(self.centralwidget)
        self.umButton.setGeometry(QtCore.QRect(10, 420, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.umButton.setFont(font)
        self.umButton.setObjectName("umButton")
        self.eraseButton = QtWidgets.QPushButton(self.centralwidget)
        self.eraseButton.setGeometry(QtCore.QRect(270, 150, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.eraseButton.setFont(font)
        self.eraseButton.setObjectName("eraseButton")
        self.divisaoButton = QtWidgets.QPushButton(self.centralwidget)
        self.divisaoButton.setGeometry(QtCore.QRect(390, 150, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.divisaoButton.setFont(font)
        self.divisaoButton.setObjectName("divisaoButton")
        self.cincoButton = QtWidgets.QPushButton(self.centralwidget)
        self.cincoButton.setGeometry(QtCore.QRect(140, 330, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.cincoButton.setFont(font)
        self.cincoButton.setObjectName("cincoButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(10, 510, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.doisButton = QtWidgets.QPushButton(self.centralwidget)
        self.doisButton.setGeometry(QtCore.QRect(140, 420, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.doisButton.setFont(font)
        self.doisButton.setObjectName("doisButton")
        self.oitoButton = QtWidgets.QPushButton(self.centralwidget)
        self.oitoButton.setGeometry(QtCore.QRect(140, 240, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.oitoButton.setFont(font)
        self.oitoButton.setObjectName("oitoButton")
        self.seisButton = QtWidgets.QPushButton(self.centralwidget)
        self.seisButton.setGeometry(QtCore.QRect(270, 330, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.seisButton.setFont(font)
        self.seisButton.setObjectName("seisButton")
        self.virgulaButton = QtWidgets.QPushButton(self.centralwidget)
        self.virgulaButton.setGeometry(QtCore.QRect(140, 510, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.virgulaButton.setFont(font)
        self.virgulaButton.setObjectName("virgulaButton")
        self.tresButton = QtWidgets.QPushButton(self.centralwidget)
        self.tresButton.setGeometry(QtCore.QRect(270, 420, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.tresButton.setFont(font)
        self.tresButton.setObjectName("tresButton")
        self.noveButton = QtWidgets.QPushButton(self.centralwidget)
        self.noveButton.setGeometry(QtCore.QRect(270, 240, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.noveButton.setFont(font)
        self.noveButton.setObjectName("noveButton")
        self.menosButton = QtWidgets.QPushButton(self.centralwidget)
        self.menosButton.setGeometry(QtCore.QRect(390, 330, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.menosButton.setFont(font)
        self.menosButton.setObjectName("menosButton")
        self.igualButton = QtWidgets.QPushButton(self.centralwidget)
        self.igualButton.setGeometry(QtCore.QRect(270, 510, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.igualButton.setFont(font)
        self.igualButton.setObjectName("igualButton")
        self.maisButton = QtWidgets.QPushButton(self.centralwidget)
        self.maisButton.setGeometry(QtCore.QRect(390, 420, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.maisButton.setFont(font)
        self.maisButton.setObjectName("maisButton")
        self.vezesButton = QtWidgets.QPushButton(self.centralwidget)
        self.vezesButton.setGeometry(QtCore.QRect(390, 240, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.vezesButton.setFont(font)
        self.vezesButton.setObjectName("vezesButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.seteButton.setText(_translate("MainWindow", "7"))
        self.quatroButton.setText(_translate("MainWindow", "4"))
        self.umButton.setText(_translate("MainWindow", "1"))
        self.eraseButton.setText(_translate("MainWindow", "<--"))
        self.divisaoButton.setText(_translate("MainWindow", "/"))
        self.cincoButton.setText(_translate("MainWindow", "5"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.doisButton.setText(_translate("MainWindow", "2"))
        self.oitoButton.setText(_translate("MainWindow", "8"))
        self.seisButton.setText(_translate("MainWindow", "6"))
        self.virgulaButton.setText(_translate("MainWindow", ","))
        self.tresButton.setText(_translate("MainWindow", "3"))
        self.noveButton.setText(_translate("MainWindow", "9"))
        self.menosButton.setText(_translate("MainWindow", "---"))
        self.igualButton.setText(_translate("MainWindow", "="))
        self.maisButton.setText(_translate("MainWindow", "+"))
        self.vezesButton.setText(_translate("MainWindow", "X"))
