import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from fatorial import Ui_MainWindow  # Importa a interface gerada

class main_fatorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.fatorar)
        
    def fatorar(self):
        try:
            num1 = int(self.ui.lineEditNumero1.text())
            
            resultado = 1
            while (num1 > 0):
                resultado = resultado * num1
                num1 = num1 -1

            self.ui.labelResultado.setText(f"Resultado: {resultado}")
            
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira números válidos!")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_fatorial()
    janela.show()
    sys.exit(app.exec_())