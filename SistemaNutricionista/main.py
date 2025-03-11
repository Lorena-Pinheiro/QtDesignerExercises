import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal
from sistemaNutricionista import Ui_MainWindow  # Importa a interface gerada

class ClickableLabel(QLabel):
    clicked = pyqtSignal()  

    def mousePressEvent(self, event):
        self.clicked.emit()  
        super().mousePressEvent(event)



class main_sistemaNutricionista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.nome = self.ui.inputNome
        self.idade = self.ui.inputIdade
        self.peso = self.ui.inputPeso
        self.altura = self.ui.inputAltura
        self.objetivo = self.ui.inputObjetivo

        lbls = ["lblPacientes", "lblAgenda", "lblDietas", "lblAdicionar", "lblCancelar", "lblSalvar"]

        for nomeLabel in lbls:
            lblAntigo = getattr(self.ui, nomeLabel, None)
            if lblAntigo and isinstance(lblAntigo, QLabel):
                lblNovo = ClickableLabel(lblAntigo.parent())
                lblNovo.setGeometry(lblAntigo.geometry())  
                lblNovo.setText(lblAntigo.text())  
                lblNovo.setStyleSheet(lblAntigo.styleSheet())  
                lblNovo.setCursor(lblAntigo.cursor())

                if nomeLabel == "lblSalvar":
                    lblNovo.clicked.connect(self.salvarEditar)
                else:
                    lblNovo.clicked.connect(self.mudarPagina)

                setattr(self.ui, nomeLabel, lblNovo)  

    def mudarPagina(self):
        sender = self.sender()
        if sender == self.ui.lblPacientes:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif sender == self.ui.lblAdicionar:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif sender == self.ui.lblCancelar:
            self.ui.stackedWidget.setCurrentIndex(1)

    def salvarEditar(self):
        userData = {
            "nome": self.nome.text(),
            "idade": self.idade.text(),
            "peso": self.peso.text(),
            "altura": self.altura.text(),
            "objetivo": self.objetivo.text(),
        }

        try:
            with open('userData.json', 'r') as file: 
                data = json.load(file)
        except (json.JSONDecodeError):
            data = []

        if userData in data:
            QMessageBox.information(self, "Aviso","Usuário já cadastrado.")
            self.nome.setText("")
            self.idade.setText("")
            self.peso.setText("")
            self.altura.setText("")
            self.objetivo.setText("")
        else:
            data.append(userData)
            with open('userData.json', 'w') as file:
                json.dump(data, file, indent=4)
            self.ui.stackedWidget.setCurrentIndex(1)
            QMessageBox.information(self, "Sucesso","Usuário cadastrado com sucesso.")
            self.nome.setText("")
            self.idade.setText("")
            self.peso.setText("")
            self.altura.setText("")
            self.objetivo.setText("")
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_sistemaNutricionista()
    janela.show()
    sys.exit(app.exec_())