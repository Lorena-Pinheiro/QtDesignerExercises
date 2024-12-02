# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jogo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 851, 621))
        self.stackedWidget.setObjectName("stackedWidget")
        self.menu = QtWidgets.QWidget()
        self.menu.setObjectName("menu")
        self.pushButtonJogar = QtWidgets.QPushButton(self.menu)
        self.pushButtonJogar.setGeometry(QtCore.QRect(250, 400, 351, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonJogar.setFont(font)
        self.pushButtonJogar.setObjectName("pushButtonJogar")
        self.pushButtonSair = QtWidgets.QPushButton(self.menu)
        self.pushButtonSair.setGeometry(QtCore.QRect(250, 480, 351, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonSair.setFont(font)
        self.pushButtonSair.setObjectName("pushButtonSair")
        self.label_5 = QtWidgets.QLabel(self.menu)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 861, 621))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imgs/BackgroundInicio.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.pushButtonJogar.raise_()
        self.pushButtonSair.raise_()
        self.stackedWidget.addWidget(self.menu)
        self.personagem = QtWidgets.QWidget()
        self.personagem.setObjectName("personagem")
        self.label = QtWidgets.QLabel(self.personagem)
        self.label.setGeometry(QtCore.QRect(270, 10, 311, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.personagem)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 191, 181))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../Downloads/charizard.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButtonEscolherCharizard = QtWidgets.QPushButton(self.personagem)
        self.pushButtonEscolherCharizard.setGeometry(QtCore.QRect(100, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonEscolherCharizard.setFont(font)
        self.pushButtonEscolherCharizard.setObjectName("pushButtonEscolherCharizard")
        self.label_8 = QtWidgets.QLabel(self.personagem)
        self.label_8.setGeometry(QtCore.QRect(350, 100, 181, 181))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../../../Downloads/snorlax.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.personagem)
        self.label_9.setGeometry(QtCore.QRect(580, 100, 191, 181))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../../Downloads/psyduck.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.personagem)
        self.label_10.setGeometry(QtCore.QRect(100, 290, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.personagem)
        self.label_11.setGeometry(QtCore.QRect(350, 290, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.personagem)
        self.label_12.setGeometry(QtCore.QRect(580, 290, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButtonEscolherSnorlax = QtWidgets.QPushButton(self.personagem)
        self.pushButtonEscolherSnorlax.setGeometry(QtCore.QRect(350, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonEscolherSnorlax.setFont(font)
        self.pushButtonEscolherSnorlax.setObjectName("pushButtonEscolherSnorlax")
        self.pushButtonEscolherPsyduck = QtWidgets.QPushButton(self.personagem)
        self.pushButtonEscolherPsyduck.setGeometry(QtCore.QRect(580, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonEscolherPsyduck.setFont(font)
        self.pushButtonEscolherPsyduck.setObjectName("pushButtonEscolherPsyduck")
        self.pushButtonLutar = QtWidgets.QPushButton(self.personagem)
        self.pushButtonLutar.setGeometry(QtCore.QRect(320, 500, 241, 71))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonLutar.setFont(font)
        self.pushButtonLutar.setObjectName("pushButtonLutar")
        self.label_13 = QtWidgets.QLabel(self.personagem)
        self.label_13.setGeometry(QtCore.QRect(0, -8, 851, 621))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../../../../Downloads/white.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_13.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButtonEscolherCharizard.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.pushButtonEscolherSnorlax.raise_()
        self.pushButtonEscolherPsyduck.raise_()
        self.pushButtonLutar.raise_()
        self.stackedWidget.addWidget(self.personagem)
        self.luta = QtWidgets.QWidget()
        self.luta.setObjectName("luta")
        self.label_3 = QtWidgets.QLabel(self.luta)
        self.label_3.setGeometry(QtCore.QRect(0, 490, 451, 101))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButtonGolpeForte = QtWidgets.QPushButton(self.luta)
        self.pushButtonGolpeForte.setGeometry(QtCore.QRect(390, 500, 121, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonGolpeForte.setFont(font)
        self.pushButtonGolpeForte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonGolpeForte.setStyleSheet("background-color: rgb(255, 229, 26);\n"
"border-color: rgb(163, 159, 32);\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButtonGolpeForte.setObjectName("pushButtonGolpeForte")
        self.pushButtonGolpeMedio = QtWidgets.QPushButton(self.luta)
        self.pushButtonGolpeMedio.setGeometry(QtCore.QRect(530, 500, 121, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonGolpeMedio.setFont(font)
        self.pushButtonGolpeMedio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonGolpeMedio.setStyleSheet("background-color: rgb(255, 229, 26);\n"
"border-color: rgb(163, 159, 32);\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButtonGolpeMedio.setObjectName("pushButtonGolpeMedio")
        self.pushButtonGolpeFraco = QtWidgets.QPushButton(self.luta)
        self.pushButtonGolpeFraco.setGeometry(QtCore.QRect(670, 500, 121, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonGolpeFraco.setFont(font)
        self.pushButtonGolpeFraco.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonGolpeFraco.setStyleSheet("background-color: rgb(255, 229, 26);\n"
"border-color: rgb(163, 159, 32);\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);")
        self.pushButtonGolpeFraco.setObjectName("pushButtonGolpeFraco")
        self.label_4 = QtWidgets.QLabel(self.luta)
        self.label_4.setGeometry(QtCore.QRect(530, 150, 231, 221))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imgs/buzzwole.webp"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.labelHPAdversario = QtWidgets.QLabel(self.luta)
        self.labelHPAdversario.setGeometry(QtCore.QRect(580, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.labelHPAdversario.setFont(font)
        self.labelHPAdversario.setObjectName("labelHPAdversario")
        self.labelPersonagemJogador = QtWidgets.QLabel(self.luta)
        self.labelPersonagemJogador.setGeometry(QtCore.QRect(20, 230, 351, 331))
        self.labelPersonagemJogador.setText("")
        self.labelPersonagemJogador.setPixmap(QtGui.QPixmap("imgs/psyduckBack.webp"))
        self.labelPersonagemJogador.setScaledContents(True)
        self.labelPersonagemJogador.setObjectName("labelPersonagemJogador")
        self.labelHPJogador = QtWidgets.QLabel(self.luta)
        self.labelHPJogador.setGeometry(QtCore.QRect(130, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.labelHPJogador.setFont(font)
        self.labelHPJogador.setObjectName("labelHPJogador")
        self.label_16 = QtWidgets.QLabel(self.luta)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 851, 471))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("imgs/BackgroundLutaTop.jpg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_14 = QtWidgets.QLabel(self.luta)
        self.label_14.setGeometry(QtCore.QRect(0, 470, 851, 141))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("imgs/BackgroundLutaBottom.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(self.luta)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 501, 131))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgs/chat.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.labelChat = QtWidgets.QLabel(self.luta)
        self.labelChat.setGeometry(QtCore.QRect(50, 30, 481, 111))
        self.labelChat.setAlignment(QtCore.Qt.AlignCenter)
        self.labelChat.setObjectName("labelChat")
        self.label_16.raise_()
        self.labelPersonagemJogador.raise_()
        self.label_4.raise_()
        self.labelHPAdversario.raise_()
        self.labelHPJogador.raise_()
        self.label_14.raise_()
        self.pushButtonGolpeForte.raise_()
        self.pushButtonGolpeMedio.raise_()
        self.pushButtonGolpeFraco.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.labelChat.raise_()
        self.stackedWidget.addWidget(self.luta)
        self.fim = QtWidgets.QWidget()
        self.fim.setObjectName("fim")
        self.label_6 = QtWidgets.QLabel(self.fim)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 851, 611))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgs/BackgroundFim.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.labelResultado = QtWidgets.QLabel(self.fim)
        self.labelResultado.setGeometry(QtCore.QRect(340, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.labelResultado.setFont(font)
        self.labelResultado.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelResultado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResultado.setObjectName("labelResultado")
        self.pushButtonSim = QtWidgets.QPushButton(self.fim)
        self.pushButtonSim.setGeometry(QtCore.QRect(310, 300, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonSim.setFont(font)
        self.pushButtonSim.setObjectName("pushButtonSim")
        self.pushButtonNao = QtWidgets.QPushButton(self.fim)
        self.pushButtonNao.setGeometry(QtCore.QRect(440, 300, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButtonNao.setFont(font)
        self.pushButtonNao.setObjectName("pushButtonNao")
        self.label_15 = QtWidgets.QLabel(self.fim)
        self.label_15.setGeometry(QtCore.QRect(330, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.fim)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonJogar.setText(_translate("MainWindow", "Jogar"))
        self.pushButtonSair.setText(_translate("MainWindow", "Sair"))
        self.label.setText(_translate("MainWindow", "Escolha seu personagem"))
        self.pushButtonEscolherCharizard.setText(_translate("MainWindow", "Escolher"))
        self.label_10.setText(_translate("MainWindow", "HP: 360\n"
" \n"
"Poderzinhos:\n"
"-- Fire Spin 30Fr\n"
"-- Scratch 40M\n"
"-- Dragon Breath 60Ft"))
        self.label_11.setText(_translate("MainWindow", "HP: 524\n"
" \n"
"Poderzinhos:\n"
"-- Lick 30Fr\n"
"-- Tackle 40M\n"
"-- Bite 60Ft"))
        self.label_12.setText(_translate("MainWindow", "HP: 360\n"
" \n"
"Poderzinhos:\n"
"-- Fire Spin 30\n"
"-- Scratch 40\n"
"-- Dragon Breath 60"))
        self.pushButtonEscolherSnorlax.setText(_translate("MainWindow", "Escolher"))
        self.pushButtonEscolherPsyduck.setText(_translate("MainWindow", "Escolher"))
        self.pushButtonLutar.setText(_translate("MainWindow", "Lutar"))
        self.label_3.setText(_translate("MainWindow", "O que você quer fazer?"))
        self.pushButtonGolpeForte.setText(_translate("MainWindow", "Forte"))
        self.pushButtonGolpeMedio.setText(_translate("MainWindow", "Medio"))
        self.pushButtonGolpeFraco.setText(_translate("MainWindow", "Fraco"))
        self.labelHPAdversario.setText(_translate("MainWindow", "HP: 107"))
        self.labelHPJogador.setText(_translate("MainWindow", "HP: "))
        self.labelChat.setText(_translate("MainWindow", "TextLabel"))
        self.labelResultado.setText(_translate("MainWindow", "Game Over"))
        self.pushButtonSim.setText(_translate("MainWindow", "SIM"))
        self.pushButtonNao.setText(_translate("MainWindow", "NÃO"))
        self.label_15.setText(_translate("MainWindow", "Jogar de novo?"))
