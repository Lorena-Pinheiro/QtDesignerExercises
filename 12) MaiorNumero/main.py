import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maioNumero import Ui_MainWindow  # Importa a interface gerada

class main_maioNumero(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.maiorNumero)
        
    def maiorNumero(self):
        n1 = int(self.ui.lineEditNum1.text())
        n2 = int(self.ui.lineEditNum2.text())
        n3 = int(self.ui.lineEditNum3.text())

        if n1 > n2 and n1 > n3:
            self.ui.labelResultado.setText(f"{n1} é o maior número")
        elif n2 > n1 and n2 > n3:
            self.ui.labelResultado.setText(f"{n2} é o maior número")
        elif n3 > n1 and n3 > n2:
            self.ui.labelResultado.setText(f"{n3} é o maior número")
        else:
            self.ui.labelResultado.setText("Nenhum número é maior")
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_maioNumero()
    janela.show()
    sys.exit(app.exec_())