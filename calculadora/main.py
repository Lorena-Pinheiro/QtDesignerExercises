import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from calculadora import Ui_MainWindow  # arquivo gerado pelo pyuic5

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.zeroButton.clicked.connect(lambda: self.apertarBotao("0"))
        self.ui.umButton.clicked.connect(lambda: self.apertarBotao("1"))
        self.ui.doisButton.clicked.connect(lambda: self.apertarBotao("2"))
        self.ui.tresButton.clicked.connect(lambda: self.apertarBotao("3"))
        self.ui.quatroButton.clicked.connect(lambda: self.apertarBotao("4"))
        self.ui.cincoButton.clicked.connect(lambda: self.apertarBotao("5"))
        self.ui.seisButton.clicked.connect(lambda: self.apertarBotao("6"))
        self.ui.seteButton.clicked.connect(lambda: self.apertarBotao("7"))
        self.ui.oitoButton.clicked.connect(lambda: self.apertarBotao("8"))
        self.ui.noveButton.clicked.connect(lambda: self.apertarBotao("9"))
        
        self.ui.maisButton.clicked.connect(self.operacao)
        self.ui.menosButton.clicked.connect(self.menos)
        self.ui.vezesButton.clicked.connect(self.vezes)
        self.ui.divisaoButton.clicked.connect(self.divisao)
        self.ui.igualButton.clicked.connect(self.igual)
        
        self.ui.clearButton.clicked.connect(self.clear)

        self.current_input = ""  
        self.operation = None   
        self.first_number = None

    def apertarBotao(self, pressed):
        self.outputLabel.setText(pressed)
        
    def ():
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())