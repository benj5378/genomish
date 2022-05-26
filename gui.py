import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main import makeDNA, makeRNA, makeProteinChain

from ui_mainwindow import Ui_MainWindow

# import main


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_run.clicked.connect(self.pushButton_run_clicked)

    def pushButton_run_clicked(self):
        DNAtemplate = self.ui.textEdit_DNA_template.toPlainText()
        DNA = makeDNA(DNAtemplate=DNAtemplate)
        self.ui.textEdit_DNA.setPlainText(DNA)
        RNA = makeRNA(DNA=DNA)
        self.ui.textEdit_mRNA.setPlainText(RNA)
        self.ui.textEdit_protein_chain.setPlainText(makeProteinChain(makeRNA(DNA)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
