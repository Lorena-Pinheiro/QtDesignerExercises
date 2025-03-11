import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from PyQt5.QtMultimedia import  QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from musicPlayer import Ui_MainWindow  # arquivo gerado pelo pyuic5

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.ui.pushButton.clicked.connect(self.playMusic)
        self.ui.pushButton_2.clicked.connect(self.stopMusic)
        self.ui.pushButton_3.clicked.connect(self.pauseMusic)

    def playMusic(self):
        caminhoMusica = os.path.abspath("musics/playItLoud.mp3")
        url = QUrl.fromLocalFile(caminhoMusica)

        if url.isValid:
            self.player.setMedia(QMediaContent(url))
            self.player.play()

    def stopMusic(self):
        self.player.stop()
        self.isPaused = False

    def pauseMusic(self):
        self.player.pause()
        self.isPaused = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())