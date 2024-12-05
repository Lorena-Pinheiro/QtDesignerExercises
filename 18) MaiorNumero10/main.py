import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maiorNumero10 import Ui_MainWindow  # Importa a interface gerada

class main_maiorNumero10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.maiorNumero10)
        self.numbers = []  
        self.counter = 0   

    def maiorNumero10(self):
        if self.counter < 10:
            n = int(self.ui.lineEditNumber.text())
            self.numbers.append(n)
            self.counter += 1
            self.ui.lineEditNumber.clear()
            if self.counter == 10:
                max_number = max(self.numbers)
                self.ui.labelResultado.setText(f"O maior número digitado é {max_number}")
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_maiorNumero10()
    janela.show()
    sys.exit(app.exec_())