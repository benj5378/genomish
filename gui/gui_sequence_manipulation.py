import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main import makeDNA, makeRNA, makeProteinChain

from gui.ui_sequence_manipulation import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_run.clicked.connect(self.pushButton_run_clicked)
        self.ui.pushButton_clear_all.clicked.connect(
            self.pushButton_clear_all_clicked)

    def sequence_to_RICH_in_color(self, sequence):
        rich = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /></head><body style=" font-family:'Courier New'; font-size:14pt; font-weight:400;">"""
        for base in sequence:
            if base == 'A':
                color = "blue"
            elif base == 'C':
                color = "red"
            elif base == 'G':
                color = "green"
            elif base == 'T' or base == 'U':
                color = "magenta"
            else:
                color = "black"
            rich = rich + """<span style="color: """ + color + """">""" + base + "</span>"
        rich = rich + "</body></html>"
        return rich

    def text_to_RICH(self, text):
        return f"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /></head>
            <body style=" font-family:'Courier New'; font-size:14pt; font-weight:400;"><span>{text}</span></body></html>"""

    def pushButton_run_clicked(self):
        color = self.sequence_to_RICH_in_color

        DNAtemplate = self.ui.textEdit_DNA_template.toPlainText()
        self.ui.textEdit_DNA_template.setHtml(color(DNAtemplate))

        DNA = makeDNA(DNAtemplate=DNAtemplate)
        self.ui.textEdit_DNA.setHtml(color(DNA))

        RNA = makeRNA(DNA=DNA)
        self.ui.textEdit_mRNA.setHtml(color(RNA))

        chain = makeProteinChain(RNA)
        self.ui.textEdit_protein_chain.setHtml(self.text_to_RICH(chain))

    def pushButton_clear_all_clicked(self):
        self.ui.textEdit_DNA.setPlainText("")
        self.ui.textEdit_DNA_template.setPlainText("")
        self.ui.textEdit_mRNA.setPlainText("")
        self.ui.textEdit_protein_chain.setPlainText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())