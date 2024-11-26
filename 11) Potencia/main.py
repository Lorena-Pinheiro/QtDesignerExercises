import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from potencia import Ui_MainWindow  # Importa a interface gerada

class main_potencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.potencia)
        
    def potencia(self):
        base = int(self.ui.lineEditBase.text())
        expoente = int(self.ui.lineEditExpoente.text())
        resultado = 1

        for i in range(expoente):
            resultado = resultado * base

        self.ui.labelResultado.setText(f"Resultado: {resultado}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_potencia()
    janela.show()
    sys.exit(app.exec_())