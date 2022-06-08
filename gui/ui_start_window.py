# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_start_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
)
from PySide6.QtWidgets import (
    QMenuBar,
    QPushButton,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 296)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_sequence_manipulation = QPushButton(self.centralwidget)
        self.pushButton_sequence_manipulation.setObjectName(
            "pushButton_sequence_manipulation"
        )
        self.pushButton_sequence_manipulation.setGeometry(QRect(10, 10, 131, 61))
        self.pushButton_sequence_alignment = QPushButton(self.centralwidget)
        self.pushButton_sequence_alignment.setObjectName(
            "pushButton_sequence_alignment"
        )
        self.pushButton_sequence_alignment.setGeometry(QRect(150, 10, 131, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 560, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.pushButton_sequence_manipulation.setText(
            QCoreApplication.translate("MainWindow", "Sequence\n" "manipulation", None)
        )
        self.pushButton_sequence_alignment.setText(
            QCoreApplication.translate("MainWindow", "Sequence\n" "alignment", None)
        )

    # retranslateUi
