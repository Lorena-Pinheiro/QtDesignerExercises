import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maiorNumero10 import Ui_MainWindow  # Importa a interface gerada

class main_maiorNumero10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonMostrar.clicked.connect(self.maiorNumero10)
        self.numeros = []  
        self.i = 0   

    def maiorNumero10(self):
        if self.i < 10:
            try:
                n = int(self.ui.lineEditNumero1.text())
            except:
                self.ui.labelResultado.setText("Digite um número válido")
                return
            self.ui.labelResultado.setText("Número enviado com sucesso. Digite o próximo")
            self.numeros.append(n)
            self.i += 1
            self.ui.lineEditNumero1.clear()
            if self.i == 10:
                max_number = max(self.numeros)
                self.ui.labelResultado.setText(f"O maior número digitado é {max_number}")
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_maiorNumero10()
    janela.show()
    sys.exit(app.exec_())