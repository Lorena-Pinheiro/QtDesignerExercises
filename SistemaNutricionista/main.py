import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QGridLayout,
    QPushButton, QFrame, QWidget, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from sistemaNutricionista_ui import Ui_MainWindow  # Import the generated UI

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

        self.scrollWidget = QWidget()
        self.userGrid = QGridLayout(self.scrollWidget)

        self.ui.scrollArea.setWidget(self.scrollWidget)

        self.paciente_editando = None  # Stores the patient being edited

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
                    lblNovo.clicked.connect(self.salvarOuAtualizarPaciente)
                elif nomeLabel == "lblPacientes":
                    lblNovo.clicked.connect(self.mostrarPacientes)
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

    def salvarOuAtualizarPaciente(self):
        if self.paciente_editando:
            self.atualizarPaciente()
        else:
            self.salvarPaciente()

    def salvarPaciente(self):
        try:
            with open('userData.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        userData = {
            "nome": self.nome.text(),
            "idade": self.idade.text(),
            "peso": self.peso.text(),
            "altura": self.altura.text(),
            "objetivo": self.objetivo.text(),
        }

        if any(p["nome"] == userData["nome"] for p in data):
            QMessageBox.information(self, "Aviso", "Usuário já cadastrado.")
        else:
            data.append(userData)
            with open('userData.json', 'w') as file:
                json.dump(data, file, indent=4)
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso.")

        self.limparCampos()
        self.mostrarPacientes()

    def atualizarPaciente(self):
        if not self.paciente_editando:
            return

        try:
            with open("userData.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        for paciente in data:
            if paciente["nome"] == self.paciente_editando["nome"]:
                paciente["nome"] = self.nome.text()
                paciente["idade"] = self.idade.text()
                paciente["peso"] = self.peso.text()
                paciente["altura"] = self.altura.text()
                paciente["objetivo"] = self.objetivo.text()
                break

        with open("userData.json", "w") as file:
            json.dump(data, file, indent=4)

        QMessageBox.information(self, "Sucesso", "Paciente atualizado com sucesso.")
        self.paciente_editando = None
        self.limparCampos()
        self.mostrarPacientes()

    def salvarEditarDeletar(self, acao, paciente):
        if acao == "U":
            self.ui.stackedWidget.setCurrentIndex(2)
            self.paciente_editando = paciente

            self.nome.setText(paciente["nome"])
            self.idade.setText(paciente["idade"])
            self.peso.setText(paciente["peso"])
            self.altura.setText(paciente["altura"])
            self.objetivo.setText(paciente["objetivo"])

        elif acao == "D":
            reply = QMessageBox.question(
                self, "Excluir Usuário", f"Tem certeza que deseja excluir {paciente['nome']}?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                try:
                    with open("userData.json", "r") as file:
                        data = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    data = []

                pacientes = [p for p in data if p["nome"] != paciente["nome"]]

                with open("userData.json", "w") as file:
                    json.dump(pacientes, file, indent=4)

                self.mostrarPacientes()

    def mostrarPacientes(self):
        try:
            with open("userData.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        for i in reversed(range(self.userGrid.count())):
            widget = self.userGrid.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        row, col = 0, 0
        for user in users:
            user_card = self.create_user_card(user)
            self.userGrid.addWidget(user_card, row, col)

            col += 1
            if col == 3:
                col = 0
                row += 1

        self.scrollWidget.setLayout(self.userGrid)
        self.ui.stackedWidget.setCurrentIndex(1)

    def create_user_card(self, paciente):
        card = QFrame()
        card.setStyleSheet("background-color: white; border: 2px solid gray; border-radius: 10px;")
        card.setFixedSize(180, 230)
        layout = QVBoxLayout(card)

        img_label = QLabel()
        pixmap = QPixmap("imgs/paciente1-removebg-preview.png")
        img_label.setPixmap(pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        img_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(img_label)

        name_label = QLabel(paciente["nome"])
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(name_label)

        btn_edit = QPushButton("EDITAR")
        btn_edit.setCursor(Qt.PointingHandCursor)
        btn_edit.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        btn_edit.clicked.connect(lambda: self.salvarEditarDeletar("U", paciente))
        layout.addWidget(btn_edit)

        btn_delete = QPushButton("EXCLUIR")
        btn_delete.setCursor(Qt.PointingHandCursor)
        btn_delete.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        btn_delete.clicked.connect(lambda: self.salvarEditarDeletar("D", paciente))
        layout.addWidget(btn_delete)

        return card

    def limparCampos(self):
        self.nome.clear()
        self.idade.clear()
        self.peso.clear()
        self.altura.clear()
        self.objetivo.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_sistemaNutricionista()
    janela.show()
    sys.exit(app.exec_())