# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTextEdit,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 559)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setGeometry(QRect(680, 460, 111, 41))
        self.textEdit_DNA = QTextEdit(self.centralwidget)
        self.textEdit_DNA.setObjectName(u"textEdit_DNA")
        self.textEdit_DNA.setGeometry(QRect(10, 40, 781, 71))
        font = QFont()
        font.setPointSize(14)
        self.textEdit_DNA.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 41, 31))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 120, 121, 31))
        self.label_2.setFont(font)
        self.textEdit_DNA_template = QTextEdit(self.centralwidget)
        self.textEdit_DNA_template.setObjectName(u"textEdit_DNA_template")
        self.textEdit_DNA_template.setGeometry(QRect(10, 150, 781, 71))
        self.textEdit_DNA_template.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 230, 61, 31))
        self.label_3.setFont(font)
        self.textEdit_mRNA = QTextEdit(self.centralwidget)
        self.textEdit_mRNA.setObjectName(u"textEdit_mRNA")
        self.textEdit_mRNA.setGeometry(QRect(10, 260, 781, 71))
        self.textEdit_mRNA.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 340, 121, 31))
        self.label_4.setFont(font)
        self.textEdit_protein_chain = QTextEdit(self.centralwidget)
        self.textEdit_protein_chain.setObjectName(u"textEdit_protein_chain")
        self.textEdit_protein_chain.setGeometry(QRect(10, 370, 781, 71))
        self.textEdit_protein_chain.setFont(font)
        self.pushButton_clear_all = QPushButton(self.centralwidget)
        self.pushButton_clear_all.setObjectName(u"pushButton_clear_all")
        self.pushButton_clear_all.setGeometry(QRect(560, 460, 111, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Genomish", None)
        )
        self.pushButton_run.setText(
            QCoreApplication.translate("MainWindow", u"RUN", None)
        )
        self.textEdit_DNA.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.label.setText(QCoreApplication.translate("MainWindow", u"DNA", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"DNA template", None)
        )
        self.textEdit_DNA_template.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3'-TACCCCAGCGGACGC-5'</p></body></html>",
                None,
            )
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"mRNA", None))
        self.textEdit_mRNA.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Protein chain", None)
        )
        self.textEdit_protein_chain.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.pushButton_clear_all.setText(
            QCoreApplication.translate("MainWindow", u"CLEAR ALL", None)
        )

    # retranslateUi
