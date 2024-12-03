import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from nota import Ui_MainWindow  # Importa a interface gerada

class main_nota(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.saberNota)
        
    def saberNota(self):
        nota = int(self.ui.lineEdit.text())
        
        if nota >= 90:
            self.ui.labelResultado.setText("Excelente")
        elif nota >= 70:
            self.ui.labelResultado.setText("Bom")
        elif nota >= 50:
            self.ui.labelResultado.setText("Regular")
        elif nota < 50:
            self.ui.labelResultado.setText("Insuficiente")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_nota()
    janela.show()
    sys.exit(app.exec_())