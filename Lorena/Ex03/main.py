import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from jogo import Ui_MainWindow  # Importa a interface gerada

class main_jogo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentIndex(0)

        self.hpJogador = 360
        self.hpAdversario = 107

        self.ui.pushButtonJogar.clicked.connect(self.mudarPagina)
        self.ui.pushButtonLutar.clicked.connect(self.mudarPagina)
        self.ui.pushButtonSim.clicked.connect(self.mudarPagina)

        self.ui.pushButtonSair.clicked.connect(self.confirmarSaida)
        self.ui.pushButtonNao.clicked.connect(self.confirmarSaida)

        self.ui.pushButtonSim.clicked.connect(self.jogoReset)

        self.ui.pushButtonEscolherCharizard.clicked.connect(self.escolherPersonagem)
        self.ui.pushButtonEscolherSnorlax.clicked.connect(self.escolherPersonagem)
        self.ui.pushButtonEscolherPsyduck.clicked.connect(self.escolherPersonagem)
        
        self.ui.pushButtonGolpeForte.clicked.connect(self.ataqueJogador)
        self.ui.pushButtonGolpeMedio.clicked.connect(self.ataqueJogador)
        self.ui.pushButtonGolpeFraco.clicked.connect(self.ataqueJogador)

        self.turnoJogador = True


    def mudarPagina(self):
        sender = self.sender()
        if sender == self.ui.pushButtonJogar:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif sender == self.ui.pushButtonLutar:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif sender == self.ui.pushButtonSim:
            self.ui.stackedWidget.setCurrentIndex(0)


    def confirmarSaida(self):
        msg = QMessageBox.question(self, 'Confirmar Saída', 'Tem certeza que deseja sair?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if msg == QMessageBox.Yes:
            self.close()


    def escolherPersonagem(self):
        sender = self.sender()
        
        self.personagens = {
            self.ui.pushButtonEscolherCharizard: {
                'image': 'imgs/charizardBack.webp',
                'hp': 360,
                'golpeForte': 'Dragon Breath',
                'golpeMedio': 'Scratch',
                'golpeFraco': 'Fire Spin'
            },
            self.ui.pushButtonEscolherSnorlax: {
                'image': 'imgs/snorlaxBack.webp',
                'hp': 524,
                'golpeForte': 'Bite',
                'golpeMedio': 'Tackle' ,
                'golpeFraco': 'Lick'
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
            pixmap = QPixmap(personagem['image'])
            self.ui.labelPersonagemJogador.setPixmap(pixmap)
            self.ui.labelPersonagemJogador.setScaledContents(True)
            self.ui.labelHPJogador.setText(f"HP: {personagem['hp']}")
            self.ui.pushButtonGolpeForte.setText(personagem['golpeForte'])
            self.ui.pushButtonGolpeMedio.setText(personagem['golpeMedio'])
            self.ui.pushButtonGolpeFraco.setText(personagem['golpeFraco'])


            self.ui.labelHPAdversario.setText(f"HP: {self.hpAdversario}")

    def ataqueJogador(self):
        if not self.turnoJogador:
            return

        sender = self.sender()
        dano = 0

        if sender == self.ui.pushButtonGolpeForte:
            dano = 60
        elif sender == self.ui.pushButtonGolpeMedio:
            dano = 40
        elif sender == self.ui.pushButtonGolpeFraco:
            dano = 30

        self.hpAdversario -= dano
        self.ui.labelHPAdversario.setText(f"HP: {self.hpAdversario}")

        if self.hpAdversario <= 0:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.labelResultado.setText("VOCÊ\nVENCEU!")
            return

        self.turnoJogador = False
        self.ataqueAdversario()

    def ataqueAdversario(self):
        if self.turnoJogador:
            return

        dano = random.choice([40, 50, 80])
        self.hpJogador -= dano
        self.ui.labelHPJogador.setText(f"HP: {self.hpJogador}")
        
        if dano == 40:
            self.ui.labelChat.setText(f"Buzzwole usou Power-Up Punch e te deu 40 de dano")
        elif dano == 50:
            self.ui.labelChat.setText(f"Buzzwole usou Fell Stinger e te deu 50 de dano")
        elif dano == 80:
            self.ui.labelChat.setText(f"Buzzwole usou Mega Punch e te deu 50 de dano")
            
        if self.hpJogador <= 0:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.labelResultado.setText("GAME\nOVER")
            return

        self.turnoJogador = True
        
    
    def jogoReset(self):
        self.hpJogador = 360
        self.hpAdversario = 107
        self.ui.labelHPJogador.setText(f"HP: {self.hpJogador}")
        self.ui.labelHPAdversario.setText(f"HP: {self.hpAdversario}")
        self.ui.labelResultado.clear()
        self.ui.stackedWidget.setCurrentIndex(0)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_jogo()
    janela.show()
    sys.exit(app.exec_())