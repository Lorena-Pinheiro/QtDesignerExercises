import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mediaAritmetica import Ui_MainWindow  # Importa a interface gerada

class main_media(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.media)
        
    def media(self):
        try:
            num1 = int(self.ui.lineEditNumero1.text())
            num2 = int(self.ui.lineEditNumero2.text())            
            num3 = int(self.ui.lineEditNumero3.text())
            
            media = (num1 + num2 + num3)/3
            
            self.ui.labelResulatdo.setText(f"Resultado: {media}")
        except ValueError:
            self.ui.labelResulatdo.setText("Por favor, insira números válidos!")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_media()
    janela.show()
    sys.exit(app.exec_())