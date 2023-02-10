import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.ui_start_window import Ui_MainWindow
from gui import gui_sequence_manipulation
from gui import gui_sequence_alignment

# import main


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_sequence_manipulation.clicked.connect(
            self.pushButton_sequence_manipulation_clicked
        )
        self.ui.pushButton_sequence_alignment.clicked.connect(
            self.pushButton_sequence_alignment_clicked
        )

    def pushButton_sequence_manipulation_clicked(self):
        gui_sequence_manipulation_window = gui_sequence_manipulation.MainWindow(self)
        gui_sequence_manipulation_window.show()

    def pushButton_sequence_alignment_clicked(self):
        gui_sequence_alignment_window = gui_sequence_alignment.MainWindow(self)
        gui_sequence_alignment_window.show()


def run():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
