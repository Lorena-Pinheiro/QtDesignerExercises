from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from listaCompra import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonAdicionar.clicked.connect(self.addMeta)
        self.pushButtonExcluir.clicked.connect(self.delMeta)
        
    def addMeta(self):
        meta = self.lineEdit.text()
        if meta:
            item = QListWidgetItem(meta)
            item.setCheckState(0)
            self.listWidget.addItem(item)
            self.lineEdit.clear()
            
    def delMeta(self):
        selectedItem = self.listWidget.currentRow()
        if selectedItem >= 0:
            self.listWidget.takeItem(selectedItem)
            
if __name__ == "__main__":
    app = QApplication([])
    window = main()
    window.show()
    app.exec_()
    