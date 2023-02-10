import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main import align

from gui.ui_sequence_alignment import Ui_MainWindow

# import main


class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_align.clicked.connect(self.pushButton_align_clicked)

    def to_RICH(self, sequence_1, sequence_2):
        return f"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /></head><body style=" font-family:'Courier New'; font-size:14pt; font-weight:400; font-style:normal;">
<span>{sequence_1}<br />{sequence_2}</span></body></html>"""

    def pushButton_align_clicked(self):
        input_sequence = self.ui.textEdit_sequence.toPlainText()
        sequence_1, sequence_2 = align(input_sequence)
        rich_html = self.to_RICH(sequence_1, sequence_2)
        self.ui.textEdit_sequence.setHtml(rich_html)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
