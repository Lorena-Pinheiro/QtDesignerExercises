import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mediaAritmeticaDinamica import Ui_MainWindow  # Importa a interface gerada

class main_mediaAritmeticaDinamica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.quantidadeNota)
        self.notas = []
        self.n = 0
        
    def quantidadeNota(self):
        try:
            self.n = int(self.ui.lineEditInput.text())
            if self.n <= 0:
                self.ui.labelResultado.setText("Digite um número maior que zero.")
                return
        except:
            self.ui.labelResultado.setText("Digite um número válido.")
            return
        
        self.ui.lineEditInput.clear()
        self.ui.labelResultado.clear()
        self.ui.labelPergunta.setText(f"Digite {self.n} notas:")
        self.ui.pushButtonEnviar.clicked.disconnect()
        self.ui.pushButtonEnviar.clicked.connect(self.media)
       
        
    def media(self):
        try:
            nota = float(self.ui.lineEditInput.text())
            if nota < 0:
                self.ui.labelResultado.setText("Digite uma nota válida.")
                return
        except ValueError:
            self.ui.labelResultado.setText("Digite um número válido.")
            return
        
        self.notas.append(nota)
        self.ui.lineEditInput.clear()

        if len(self.notas) == self.n:
            soma = sum(self.notas)
            media = soma / self.n
            self.ui.labelResultado.setText(f"A média é {media:.2f}")
            self.ui.labelPergunta.setText("Digite o número de notas a serem inseridas:")
            self.ui.pushButtonEnviar.clicked.disconnect()
            self.ui.pushButtonEnviar.clicked.connect(self.quantidadeNota)
            self.notas = []
        else:
            self.ui.labelResultado.setText(f"Digite mais {self.n - len(self.notas)} notas.")
        
    # def mediaAritmeticaDinamica(self):
    #     try:
    #         n = int(self.ui.lineEditInput.text())
    #     except:
    #         self.ui.labelResultado.setText("Digite um número válido")
    #         return
        
    #     for i in range(n):
    #         self.ui.labelResultado.clear()
    #         self.ui.lineEditInput.clear()
    #         x = n - (n+1)
    #         self.ui.labelPergunta.setText(f"Informe a {x}° nota: ")
    #         try:
    #             n2 = int(self.ui.lineEditInput.text())
    #         except:
    #             self.ui.labelResultado.setText("Digite um número válido")
    #             return
    #         self.notas.append(n2)
    #         i = i+1
            
    #     media = sum(self.notas)/n
    #     self.ui.labelResultado.setText(f"A média é {media}")
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_mediaAritmeticaDinamica()
    janela.show()
    sys.exit(app.exec_())