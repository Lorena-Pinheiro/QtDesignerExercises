import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from somaFatorial import Ui_MainWindow  # Importa a interface gerada

class main_somaFatorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.somaFatorial)
        
    def somaFatorial(self):
        num1 = int(self.ui.lineEditNumero1.text())
        soma = 0
        i = 0

        while i <= num1:
            soma = soma + i
            i = i + 1

        self.ui.labelResultado.setText(f"Resultado: {soma}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_somaFatorial()
    janela.show()
    sys.exit(app.exec_())