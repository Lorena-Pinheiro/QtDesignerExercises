import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tela1 import Ui_MainWindow as UI_Tela1
from tela2 import Ui_MainWindow as UI_Tela2

class tela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_Tela1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.abrirSegundaTela)


    def abrirSegundaTela(self):
        self.segundaTela = tela2()
        for i in range(6):
            self.segundaTela.show()
            self.close()

class tela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_Tela2()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.abrirPrimeiraTela)

    def abrirPrimeiraTela(self):
        self.primeiraTela = tela1()
        self.primeiraTela.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = tela1()
    main_window.show()
    sys.exit(app.exec_())