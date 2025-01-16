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
        
        self.ui.maisButton.clicked.connect(lambda: self.operacao("+"))
        self.ui.menosButton.clicked.connect(lambda: self.operacao("-"))
        self.ui.vezesButton.clicked.connect(lambda: self.operacao("*"))
        self.ui.divisaoButton.clicked.connect(lambda: self.operacao("/"))
        
        self.ui.igualButton.clicked.connect(self.igual)
        self.ui.clearButton.clicked.connect(self.clear)

        self.inputAtual = ""  
        self.simbolo = None   
        self.num1 = None
        
        self.lista = []

    def apertarBotao(self, numero):
        self.inputAtual += numero
        self.lista.append(self.inputAtual)
        self.ui.outputLabel.setText(' '.join(self.lista))
        
    def operacao(self, op):
        self.num1 = float(self.inputAtual)
        self.simbolo = op
        self.inputAtual = ""
        self.lista.append(f" {self.simbolo}")
        self.ui.outputLabel.setText(' '.join(self.lista))
    
    def igual(self):
        self.num2 = self.inputAtual
        self.lista.append(f" {self.num2}")
        self.ui.outputLabel.setText(' '.join(self.lista))
        
        resultado = float(eval(' '.join(self.lista)))
        self.ui.outputLabel.setText(resultado)
        
    def clear(self):
        self.inputAtual = ""
        self.num1 = None
        self.simbolo = None
        self.ui.outputLabel.setText("0")
        
        
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())
    