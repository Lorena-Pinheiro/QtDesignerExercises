# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistemaNutricionista.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1111, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.label = QtWidgets.QLabel(self.Inicio)
        self.label.setGeometry(QtCore.QRect(0, 0, 1111, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Inicio)
        self.label_2.setGeometry(QtCore.QRect(210, 160, 211, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgs/paciente-removebg-preview.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Inicio)
        self.label_3.setGeometry(QtCore.QRect(470, 180, 191, 181))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imgs/agenda-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Inicio)
        self.label_4.setGeometry(QtCore.QRect(730, 180, 191, 181))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imgs/dietas-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lblPacientes = QtWidgets.QLabel(self.Inicio)
        self.lblPacientes.setGeometry(QtCore.QRect(210, 370, 211, 51))
        self.lblPacientes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblPacientes.setText("")
        self.lblPacientes.setPixmap(QtGui.QPixmap("imgs/btnPacientes.png"))
        self.lblPacientes.setScaledContents(True)
        self.lblPacientes.setObjectName("lblPacientes")
        self.lblAgenda = QtWidgets.QLabel(self.Inicio)
        self.lblAgenda.setGeometry(QtCore.QRect(460, 370, 211, 51))
        self.lblAgenda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblAgenda.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lblAgenda.setText("")
        self.lblAgenda.setPixmap(QtGui.QPixmap("imgs/btnAgenda.png"))
        self.lblAgenda.setScaledContents(True)
        self.lblAgenda.setObjectName("lblAgenda")
        self.lblDietas = QtWidgets.QLabel(self.Inicio)
        self.lblDietas.setGeometry(QtCore.QRect(720, 370, 211, 51))
        self.lblDietas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblDietas.setText("")
        self.lblDietas.setPixmap(QtGui.QPixmap("imgs/btnDietas.png"))
        self.lblDietas.setScaledContents(True)
        self.lblDietas.setObjectName("lblDietas")
        self.stackedWidget.addWidget(self.Inicio)
        self.pacientes = QtWidgets.QWidget()
        self.pacientes.setObjectName("pacientes")
        self.bgPaciente = QtWidgets.QLabel(self.pacientes)
        self.bgPaciente.setGeometry(QtCore.QRect(0, 0, 1111, 651))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bgPaciente.setFont(font)
        self.bgPaciente.setStyleSheet("")
        self.bgPaciente.setText("")
        self.bgPaciente.setPixmap(QtGui.QPixmap("imgs/bg.jpg"))
        self.bgPaciente.setScaledContents(True)
        self.bgPaciente.setObjectName("bgPaciente")
        self.barraBusca = QtWidgets.QLineEdit(self.pacientes)
        self.barraBusca.setGeometry(QtCore.QRect(180, 100, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.barraBusca.setFont(font)
        self.barraBusca.setObjectName("barraBusca")
        self.lblBuscar = QtWidgets.QLabel(self.pacientes)
        self.lblBuscar.setGeometry(QtCore.QRect(850, 100, 51, 51))
        self.lblBuscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblBuscar.setText("")
        self.lblBuscar.setPixmap(QtGui.QPixmap("imgs/buscar.png"))
        self.lblBuscar.setScaledContents(True)
        self.lblBuscar.setObjectName("lblBuscar")
        self.lblAdicionar = QtWidgets.QLabel(self.pacientes)
        self.lblAdicionar.setGeometry(QtCore.QRect(900, 100, 51, 51))
        self.lblAdicionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblAdicionar.setText("")
        self.lblAdicionar.setPixmap(QtGui.QPixmap("imgs/plus (1).png"))
        self.lblAdicionar.setScaledContents(True)
        self.lblAdicionar.setObjectName("lblAdicionar")
        self.label_5 = QtWidgets.QLabel(self.pacientes)
        self.label_5.setGeometry(QtCore.QRect(470, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lblFotoPaciente = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente.setGeometry(QtCore.QRect(180, 190, 131, 131))
        self.lblFotoPaciente.setText("")
        self.lblFotoPaciente.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente.setScaledContents(True)
        self.lblFotoPaciente.setObjectName("lblFotoPaciente")
        self.lblEditar = QtWidgets.QLabel(self.pacientes)
        self.lblEditar.setGeometry(QtCore.QRect(170, 320, 151, 41))
        self.lblEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar.setText("")
        self.lblEditar.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar.setScaledContents(True)
        self.lblEditar.setObjectName("lblEditar")
        self.lblExcluir = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir.setGeometry(QtCore.QRect(170, 360, 151, 41))
        self.lblExcluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir.setText("")
        self.lblExcluir.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir.setScaledContents(True)
        self.lblExcluir.setObjectName("lblExcluir")
        self.lblEditar_2 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_2.setGeometry(QtCore.QRect(330, 320, 151, 41))
        self.lblEditar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_2.setText("")
        self.lblEditar_2.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_2.setScaledContents(True)
        self.lblEditar_2.setObjectName("lblEditar_2")
        self.lblExcluir_2 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_2.setGeometry(QtCore.QRect(330, 360, 151, 41))
        self.lblExcluir_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_2.setText("")
        self.lblExcluir_2.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_2.setScaledContents(True)
        self.lblExcluir_2.setObjectName("lblExcluir_2")
        self.lblFotoPaciente_2 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_2.setGeometry(QtCore.QRect(340, 190, 131, 131))
        self.lblFotoPaciente_2.setText("")
        self.lblFotoPaciente_2.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_2.setScaledContents(True)
        self.lblFotoPaciente_2.setObjectName("lblFotoPaciente_2")
        self.lblEditar_3 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_3.setGeometry(QtCore.QRect(490, 320, 151, 41))
        self.lblEditar_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_3.setText("")
        self.lblEditar_3.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_3.setScaledContents(True)
        self.lblEditar_3.setObjectName("lblEditar_3")
        self.lblExcluir_3 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_3.setGeometry(QtCore.QRect(490, 360, 151, 41))
        self.lblExcluir_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_3.setText("")
        self.lblExcluir_3.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_3.setScaledContents(True)
        self.lblExcluir_3.setObjectName("lblExcluir_3")
        self.lblFotoPaciente_3 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_3.setGeometry(QtCore.QRect(500, 190, 131, 131))
        self.lblFotoPaciente_3.setText("")
        self.lblFotoPaciente_3.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_3.setScaledContents(True)
        self.lblFotoPaciente_3.setObjectName("lblFotoPaciente_3")
        self.lblEditar_4 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_4.setGeometry(QtCore.QRect(650, 320, 151, 41))
        self.lblEditar_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_4.setText("")
        self.lblEditar_4.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_4.setScaledContents(True)
        self.lblEditar_4.setObjectName("lblEditar_4")
        self.lblExcluir_4 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_4.setGeometry(QtCore.QRect(650, 360, 151, 41))
        self.lblExcluir_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_4.setText("")
        self.lblExcluir_4.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_4.setScaledContents(True)
        self.lblExcluir_4.setObjectName("lblExcluir_4")
        self.lblFotoPaciente_4 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_4.setGeometry(QtCore.QRect(660, 190, 131, 131))
        self.lblFotoPaciente_4.setText("")
        self.lblFotoPaciente_4.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_4.setScaledContents(True)
        self.lblFotoPaciente_4.setObjectName("lblFotoPaciente_4")
        self.lblEditar_5 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_5.setGeometry(QtCore.QRect(810, 320, 151, 41))
        self.lblEditar_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_5.setText("")
        self.lblEditar_5.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_5.setScaledContents(True)
        self.lblEditar_5.setObjectName("lblEditar_5")
        self.lblExcluir_5 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_5.setGeometry(QtCore.QRect(810, 360, 151, 41))
        self.lblExcluir_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_5.setText("")
        self.lblExcluir_5.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_5.setScaledContents(True)
        self.lblExcluir_5.setObjectName("lblExcluir_5")
        self.lblFotoPaciente_5 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_5.setGeometry(QtCore.QRect(820, 190, 131, 131))
        self.lblFotoPaciente_5.setText("")
        self.lblFotoPaciente_5.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_5.setScaledContents(True)
        self.lblFotoPaciente_5.setObjectName("lblFotoPaciente_5")
        self.lblEditar_6 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_6.setGeometry(QtCore.QRect(650, 560, 151, 41))
        self.lblEditar_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_6.setText("")
        self.lblEditar_6.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_6.setScaledContents(True)
        self.lblEditar_6.setObjectName("lblEditar_6")
        self.lblEditar_7 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_7.setGeometry(QtCore.QRect(170, 560, 151, 41))
        self.lblEditar_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_7.setText("")
        self.lblEditar_7.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_7.setScaledContents(True)
        self.lblEditar_7.setObjectName("lblEditar_7")
        self.lblExcluir_6 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_6.setGeometry(QtCore.QRect(490, 600, 151, 41))
        self.lblExcluir_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_6.setText("")
        self.lblExcluir_6.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_6.setScaledContents(True)
        self.lblExcluir_6.setObjectName("lblExcluir_6")
        self.lblEditar_8 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_8.setGeometry(QtCore.QRect(810, 560, 151, 41))
        self.lblEditar_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_8.setText("")
        self.lblEditar_8.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_8.setScaledContents(True)
        self.lblEditar_8.setObjectName("lblEditar_8")
        self.lblExcluir_7 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_7.setGeometry(QtCore.QRect(810, 600, 151, 41))
        self.lblExcluir_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_7.setText("")
        self.lblExcluir_7.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_7.setScaledContents(True)
        self.lblExcluir_7.setObjectName("lblExcluir_7")
        self.lblExcluir_8 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_8.setGeometry(QtCore.QRect(650, 600, 151, 41))
        self.lblExcluir_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_8.setText("")
        self.lblExcluir_8.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_8.setScaledContents(True)
        self.lblExcluir_8.setObjectName("lblExcluir_8")
        self.lblFotoPaciente_6 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_6.setGeometry(QtCore.QRect(500, 430, 131, 131))
        self.lblFotoPaciente_6.setText("")
        self.lblFotoPaciente_6.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_6.setScaledContents(True)
        self.lblFotoPaciente_6.setObjectName("lblFotoPaciente_6")
        self.lblEditar_9 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_9.setGeometry(QtCore.QRect(330, 560, 151, 41))
        self.lblEditar_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_9.setText("")
        self.lblEditar_9.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_9.setScaledContents(True)
        self.lblEditar_9.setObjectName("lblEditar_9")
        self.lblFotoPaciente_7 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_7.setGeometry(QtCore.QRect(820, 430, 131, 131))
        self.lblFotoPaciente_7.setText("")
        self.lblFotoPaciente_7.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_7.setScaledContents(True)
        self.lblFotoPaciente_7.setObjectName("lblFotoPaciente_7")
        self.lblFotoPaciente_8 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_8.setGeometry(QtCore.QRect(660, 430, 131, 131))
        self.lblFotoPaciente_8.setText("")
        self.lblFotoPaciente_8.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_8.setScaledContents(True)
        self.lblFotoPaciente_8.setObjectName("lblFotoPaciente_8")
        self.lblExcluir_9 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_9.setGeometry(QtCore.QRect(330, 600, 151, 41))
        self.lblExcluir_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_9.setText("")
        self.lblExcluir_9.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_9.setScaledContents(True)
        self.lblExcluir_9.setObjectName("lblExcluir_9")
        self.lblExcluir_10 = QtWidgets.QLabel(self.pacientes)
        self.lblExcluir_10.setGeometry(QtCore.QRect(170, 600, 151, 41))
        self.lblExcluir_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblExcluir_10.setText("")
        self.lblExcluir_10.setPixmap(QtGui.QPixmap("imgs/btnExcluir.png"))
        self.lblExcluir_10.setScaledContents(True)
        self.lblExcluir_10.setObjectName("lblExcluir_10")
        self.lblEditar_10 = QtWidgets.QLabel(self.pacientes)
        self.lblEditar_10.setGeometry(QtCore.QRect(490, 560, 151, 41))
        self.lblEditar_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblEditar_10.setText("")
        self.lblEditar_10.setPixmap(QtGui.QPixmap("imgs/btnEditar.png"))
        self.lblEditar_10.setScaledContents(True)
        self.lblEditar_10.setObjectName("lblEditar_10")
        self.lblFotoPaciente_9 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_9.setGeometry(QtCore.QRect(340, 430, 131, 131))
        self.lblFotoPaciente_9.setText("")
        self.lblFotoPaciente_9.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_9.setScaledContents(True)
        self.lblFotoPaciente_9.setObjectName("lblFotoPaciente_9")
        self.lblFotoPaciente_10 = QtWidgets.QLabel(self.pacientes)
        self.lblFotoPaciente_10.setGeometry(QtCore.QRect(180, 430, 131, 131))
        self.lblFotoPaciente_10.setText("")
        self.lblFotoPaciente_10.setPixmap(QtGui.QPixmap("imgs/paciente1-removebg-preview.png"))
        self.lblFotoPaciente_10.setScaledContents(True)
        self.lblFotoPaciente_10.setObjectName("lblFotoPaciente_10")
        self.lblUserName = QtWidgets.QLabel(self.pacientes)
        self.lblUserName.setGeometry(QtCore.QRect(180, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName.setFont(font)
        self.lblUserName.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName.setObjectName("lblUserName")
        self.lblUserName_2 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_2.setGeometry(QtCore.QRect(340, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_2.setFont(font)
        self.lblUserName_2.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_2.setObjectName("lblUserName_2")
        self.lblUserName_3 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_3.setGeometry(QtCore.QRect(660, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_3.setFont(font)
        self.lblUserName_3.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_3.setObjectName("lblUserName_3")
        self.lblUserName_4 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_4.setGeometry(QtCore.QRect(500, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_4.setFont(font)
        self.lblUserName_4.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_4.setObjectName("lblUserName_4")
        self.lblUserName_5 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_5.setGeometry(QtCore.QRect(820, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_5.setFont(font)
        self.lblUserName_5.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_5.setObjectName("lblUserName_5")
        self.lblUserName_6 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_6.setGeometry(QtCore.QRect(340, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_6.setFont(font)
        self.lblUserName_6.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_6.setObjectName("lblUserName_6")
        self.lblUserName_7 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_7.setGeometry(QtCore.QRect(820, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_7.setFont(font)
        self.lblUserName_7.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_7.setObjectName("lblUserName_7")
        self.lblUserName_8 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_8.setGeometry(QtCore.QRect(500, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_8.setFont(font)
        self.lblUserName_8.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_8.setObjectName("lblUserName_8")
        self.lblUserName_9 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_9.setGeometry(QtCore.QRect(180, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_9.setFont(font)
        self.lblUserName_9.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_9.setObjectName("lblUserName_9")
        self.lblUserName_10 = QtWidgets.QLabel(self.pacientes)
        self.lblUserName_10.setGeometry(QtCore.QRect(660, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUserName_10.setFont(font)
        self.lblUserName_10.setStyleSheet("background-color: rgba(50, 50, 50, 150);\n"
"color: white;  \n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.lblUserName_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserName_10.setObjectName("lblUserName_10")
        self.stackedWidget.addWidget(self.pacientes)
        self.cadastrarPaciente = QtWidgets.QWidget()
        self.cadastrarPaciente.setObjectName("cadastrarPaciente")
        self.label_6 = QtWidgets.QLabel(self.cadastrarPaciente)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1111, 651))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgs/bg.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.lblFotoPacienteC = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblFotoPacienteC.setGeometry(QtCore.QRect(40, 130, 271, 281))
        self.lblFotoPacienteC.setText("")
        self.lblFotoPacienteC.setPixmap(QtGui.QPixmap("imgs/ProfilePictureBetter-removebg-preview.png"))
        self.lblFotoPacienteC.setScaledContents(True)
        self.lblFotoPacienteC.setObjectName("lblFotoPacienteC")
        self.inputNome = QtWidgets.QLineEdit(self.cadastrarPaciente)
        self.inputNome.setGeometry(QtCore.QRect(410, 90, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputNome.setFont(font)
        self.inputNome.setObjectName("inputNome")
        self.lblNome = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblNome.setGeometry(QtCore.QRect(410, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lblNome.setObjectName("lblNome")
        self.lblidade = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblidade.setGeometry(QtCore.QRect(410, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblidade.setFont(font)
        self.lblidade.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lblidade.setObjectName("lblidade")
        self.inputIdade = QtWidgets.QLineEdit(self.cadastrarPaciente)
        self.inputIdade.setGeometry(QtCore.QRect(410, 170, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputIdade.setFont(font)
        self.inputIdade.setObjectName("inputIdade")
        self.lblPeso = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblPeso.setGeometry(QtCore.QRect(410, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblPeso.setFont(font)
        self.lblPeso.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lblPeso.setObjectName("lblPeso")
        self.inputPeso = QtWidgets.QLineEdit(self.cadastrarPaciente)
        self.inputPeso.setGeometry(QtCore.QRect(410, 250, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputPeso.setFont(font)
        self.inputPeso.setObjectName("inputPeso")
        self.lblAltura = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblAltura.setGeometry(QtCore.QRect(410, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblAltura.setFont(font)
        self.lblAltura.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lblAltura.setObjectName("lblAltura")
        self.inputAltura = QtWidgets.QLineEdit(self.cadastrarPaciente)
        self.inputAltura.setGeometry(QtCore.QRect(410, 330, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputAltura.setFont(font)
        self.inputAltura.setObjectName("inputAltura")
        self.lblObjetivo = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblObjetivo.setGeometry(QtCore.QRect(410, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblObjetivo.setFont(font)
        self.lblObjetivo.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lblObjetivo.setObjectName("lblObjetivo")
        self.inputObjetivo = QtWidgets.QLineEdit(self.cadastrarPaciente)
        self.inputObjetivo.setGeometry(QtCore.QRect(410, 410, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputObjetivo.setFont(font)
        self.inputObjetivo.setObjectName("inputObjetivo")
        self.lblSexo = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblSexo.setGeometry(QtCore.QRect(410, 470, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lblSexo.setObjectName("lblSexo")
        self.rbtnMulher = QtWidgets.QRadioButton(self.cadastrarPaciente)
        self.rbtnMulher.setGeometry(QtCore.QRect(490, 480, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rbtnMulher.setFont(font)
        self.rbtnMulher.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnMulher.setObjectName("rbtnMulher")
        self.rbtnHomem = QtWidgets.QRadioButton(self.cadastrarPaciente)
        self.rbtnHomem.setGeometry(QtCore.QRect(590, 480, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rbtnHomem.setFont(font)
        self.rbtnHomem.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnHomem.setObjectName("rbtnHomem")
        self.rbtnOutro = QtWidgets.QRadioButton(self.cadastrarPaciente)
        self.rbtnOutro.setGeometry(QtCore.QRect(690, 480, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rbtnOutro.setFont(font)
        self.rbtnOutro.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnOutro.setObjectName("rbtnOutro")
        self.lblCancelar = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblCancelar.setGeometry(QtCore.QRect(720, 550, 221, 101))
        self.lblCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblCancelar.setText("")
        self.lblCancelar.setPixmap(QtGui.QPixmap("imgs/btnCancelar.png"))
        self.lblCancelar.setScaledContents(True)
        self.lblCancelar.setObjectName("lblCancelar")
        self.lblSalvar = QtWidgets.QLabel(self.cadastrarPaciente)
        self.lblSalvar.setGeometry(QtCore.QRect(370, 560, 221, 91))
        self.lblSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblSalvar.setText("")
        self.lblSalvar.setPixmap(QtGui.QPixmap("imgs/btnSalvar.png"))
        self.lblSalvar.setScaledContents(True)
        self.lblSalvar.setObjectName("lblSalvar")
        self.label_7 = QtWidgets.QLabel(self.cadastrarPaciente)
        self.label_7.setGeometry(QtCore.QRect(70, 160, 211, 221))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgs/paciente1.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_6.raise_()
        self.inputNome.raise_()
        self.lblNome.raise_()
        self.lblidade.raise_()
        self.inputIdade.raise_()
        self.lblPeso.raise_()
        self.inputPeso.raise_()
        self.lblAltura.raise_()
        self.inputAltura.raise_()
        self.lblObjetivo.raise_()
        self.inputObjetivo.raise_()
        self.lblSexo.raise_()
        self.rbtnMulher.raise_()
        self.rbtnHomem.raise_()
        self.rbtnOutro.raise_()
        self.lblCancelar.raise_()
        self.lblSalvar.raise_()
        self.label_7.raise_()
        self.lblFotoPacienteC.raise_()
        self.stackedWidget.addWidget(self.cadastrarPaciente)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
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
        self.label_5.setText(_translate("MainWindow", "PACIENTES"))
        self.lblUserName.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_2.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_3.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_4.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_5.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_6.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_7.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_8.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_9.setText(_translate("MainWindow", "Nome"))
        self.lblUserName_10.setText(_translate("MainWindow", "Nome"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblidade.setText(_translate("MainWindow", "Idade"))
        self.lblPeso.setText(_translate("MainWindow", "Peso"))
        self.lblAltura.setText(_translate("MainWindow", "Altura"))
        self.lblObjetivo.setText(_translate("MainWindow", "Objetivo"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo:"))
        self.rbtnMulher.setText(_translate("MainWindow", "Mulher"))
        self.rbtnHomem.setText(_translate("MainWindow", "Homem"))
        self.rbtnOutro.setText(_translate("MainWindow", "Outro"))
