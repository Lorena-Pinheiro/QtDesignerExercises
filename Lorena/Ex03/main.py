import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from jogoLuta import Ui_MainWindow  # Importa a interface gerada

class main_jogoLuta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonJogar.clicked.connect(self.mudarPagina())
        self.ui.pushButtonLutar.clicked.connect(self.mudarPagina())
        self.ui.pushButtonSim.clicked.connect(self.mudarPagina())

        self.ui.pushButtonSair.clicked.connect(self.confirmarSaida)
        self.ui.pushButtonNao.clicked.connect(self.confirmarSaida)

        self.ui.pushButtonEscolherCharizard.clicked.connect(self.escolherPersonagem)
        self.ui.pushButtonEscolherSnorlax.clicked.connect(self.escolherPersonagem)
        self.ui.pushButtonEscolherPsyduck.clicked.connect(self.escolherPersonagem)

        self.turnoJogador = True


    def mudarPagina(self):
        sender = self.sender()
        if sender == self.ui.pushButtonJogar:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif sender == self.ui.pushButtonLutar:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif sender == self.ui.pushButtonSim:
            self.ui.stackedWidget.setCurrentIndex(0)


    # def confirmarSaida(self):
    #     reply = QMessageBox.question(self, 'Confirm Exit', 'Are you sure you want to exit?',
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    #     if reply == QMessageBox.Yes:
    #         self.close()


    def escolherPersonagem(self):
        sender = self.sender()
        
        self.personagens = {
            self.ui.pushButtonEscolherCharizard: {
                'image': 'imgs/charizardBack.webp',
                'hp': 360,
                'golpeForte': 'Bite',
                'golpeMedio': 'Tackle',
                'golpeFraco': 'Lick'
            },
            self.ui.pushButtonEscolherSnorlax: {
                'image': 'imgs/snorlaxBack.webp',
                'hp': 524,
                'golpeForte': 'Dragon Breath',
                'golpeMedio': 'Scratch',
                'golpeFraco': 'Fire Spin'
            },
            self.ui.pushButtonEscolherPsyduck: {
                'image': 'imgs/psyduckBack.webp',
                'hp': 360,
                'golpeForte': 'Dragon Breath',
                'golpeMedio': 'Scratch',
                'golpeFraco': 'Fire Spin'
            }
        }

        personagem = self.personagens.get(sender)

        if personagem:
            self.labelPersonagemJogador.setPixmap(personagem['image'])
            self.labelPersonagemJogador.setScaledContents(True)
            self.labelHPJogador.setText(f"HP: {personagem['hp']}")
            self.pushButtonGolpeForte.setText(personagem['golpeForte'])
            self.pushButtonGolpeMedio.setText(personagem['golpeMedio'])
            self.pushButtonGolpeFraco.setText(personagem['golpeFraco'])


    def ataqueJogador(self):
        if self.turnoJogador != True:
            return

        sender = self.sender()
        vidaAdv = 107

        if sender == self.ui.pushButtonGolpeForte:
            self.ui.labelHPAdversario.setText(f"HP: {vidaAdv-60}")
        elif sender == self.ui.pushButtonGolpeMedio:
            self.ui.labelHPAdversario.setText(f"HP: {vidaAdv-40}")
        elif sender == self.ui.pushButtonGolpeFraco:
            self.ui.labelHPAdversario.setText(f"HP: {vidaAdv-30}")

        self.turnoJogador = False
        self.ataqueAdversario()

    def ataqueAdversario(self):
        if self.turnoJogador == True:
            return

        vidaJogador = int(self.labelHPJogador.text().split(": ")[1])
        golpes = [30, 40, 60]
        dano = random.choice(golpes)

        novaVidaJogador = vidaJogador - dano
        self.ui.labelHPJogador.setText(f"HP: {novaVidaJogador}")

        if novaVidaJogador <= 0:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.labelResultado.setText("GAME\nOVER")

        self.turnoJogador = True

        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_jogoLuta()
    janela.show()
    sys.exit(app.exec_())