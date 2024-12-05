import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pares1a100 import Ui_MainWindow  # Importa a interface gerada

class main_pares1a100(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.pushButtonMostrar.clicked.connect(self.pares1a100)
       
    def pares1a100(self):    
        soma = 0

        for i in range(101):
            if i % 2 == 0:
                soma += 1
        self.ui.labelResultado.setText(f"Tem {soma} números pares entre 1 e 100")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_pares1a100()
    janela.show()
    sys.exit(app.exec_())