import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from idade import Ui_MainWindow  # Importa a interface gerada

class main_idade(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.ui.pushButtonSair.clicked.connect(self.confirmarSaida)
        self.ui.pushButtonSair2.clicked.connect(self.confirmarSaida)
        
        self.ui.pushButtonVoltar.clicked.connect(self.mudarPagina)
        self.ui.pushButtonVoltar2.clicked.connect(self.mudarPagina)
        
        self.ui.pushButtonEnviar.clicked.connect(self.idade)
        
        
        
    def idade(self):
        idade = int(self.ui.lineEditAno.text())
        dataAtual = datetime.datetime.now()
        anoAtual = dataAtual.year
        
        conta = anoAtual - idade 
        
        if conta >= 18:
            self.ui.labelResultadoPode.setText("Aeeee\nVocê é maior de idade\nVocê pode jogar :D")
            self.ui.stackedWidget.setCurrentIndex(2)
        else:
            self.ui.labelResultadoNaoPode.setText("Oh não\nVocê não é maior de idade\nVocê não pode jogar :(")
            self.ui.stackedWidget.setCurrentIndex(1)
            
            
    def mudarPagina(self):
        self.ui.stackedWidget.setCurrentIndex(0)
            
    
    def confirmarSaida(self):
        msg = QMessageBox.question(self, 'Confirmar Saída', 'Tem certeza que deseja sair?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if msg == QMessageBox.Yes:
            self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_idade()
    janela.show()
    sys.exit(app.exec_())