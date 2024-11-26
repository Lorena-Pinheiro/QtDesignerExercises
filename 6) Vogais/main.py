import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from vogais import Ui_MainWindow  # Importa a interface gerada

class main_vogais(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.vogais)
        
    def vogais(self):
        string = self.ui.lineEditPalavra.text()

        a = string.count("a")
        e = string.count("e")
        i = string.count("i")
        o = string.count("o")
        u = string.count("u")

        total = a + e + i + o + u

        self.ui.labelResultado.setText(f"Há {total} vogais em sua palavra.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_vogais()
    janela.show()
    sys.exit(app.exec_())