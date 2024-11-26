import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maiorNumero import Ui_MainWindow  # Importa a interface gerada

class main_maiorNumero(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.maiorNumero)
        
    def maiorNumero(self):
        num1 = int(self.ui.lineEditNumero1.text())
        num2 = int(self.ui.lineEditNumero2.text())
        num3 = int(self.ui.lineEditNumero3.text())
        
        if num1 > num2 and num1 > num3:
            self.ui.labelResultado.setText(f"{num1} é o maior número")
        elif num2 > num1 and num2 > num3:
            self.ui.labelResultado.setText(f"{num2} é o maior número")
        elif num3 > num1 and num3 > num2:
            self.ui.labelResultado.setText(f"{num3} é o maior número")
        else:
            self.ui.labelResultado.setText("Nenhum número é maior")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_maiorNumero()
    janela.show()
    sys.exit(app.exec_())