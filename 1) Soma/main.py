import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from soma import Ui_MainWindow  # Importa a interface gerada

class main_soma(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.pushButtonSomar.clicked.connect(self.somar_numeros)
    
    def somar_numeros(self):
        try:
            # Ler os números dos campos de entrada
            num1 = int(self.ui.lineEditNumero1.text())
            num2 = int(self.ui.lineEditNumero2.text())
            
            # Calcular a soma
            soma = num1 + num2
            
            # Mostrar o resultado no rótulo
            self.ui.labelResulatdo.setText(f"Resultado: {soma}")
        except ValueError:
            self.ui.labelResulatdo.setText("Por favor, insira números válidos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_soma()
    janela.show()
    sys.exit(app.exec_())