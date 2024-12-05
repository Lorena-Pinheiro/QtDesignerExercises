import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from somaImpares import Ui_MainWindow  # Importa a interface gerada

class main_somaImpares(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.pushButtonMostrar.clicked.connect(self.somaImpares)
        
    def somaImpares(self):
        soma = 0
        i = 1

        while i < 50:
            if i % 2 != 0:
                soma += i
            i += 1
        self.ui.labelResultado.setText(f"A soma de todos os números ímpares entre 1 e 50 é {soma}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_somaImpares()
    janela.show()
    sys.exit(app.exec_())