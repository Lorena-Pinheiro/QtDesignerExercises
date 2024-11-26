import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio1 import Ui_MainWindow

class Exercicio1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.exibir_nome_idade)
        
    def exibir_nome_idade(self):
        nome = self.lineEditNome.text()
        idade = self.lineEditIdade.text()
        
        self.labelResultado.setText(f"Nome: {nome}, Idade: {idade}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Exercicio1()
    window.show()
    sys.exit(app.exec_())