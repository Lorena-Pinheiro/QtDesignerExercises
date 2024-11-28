import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from jogoLuta import Ui_MainWindow  # Importa a interface gerada

class main_jogoLuta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_jogoLuta()
    janela.show()
    sys.exit(app.exec_())