# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mode_select.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(581, 441)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 580, 440))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 80%);\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(90, 100, 381, 221))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: #FFFFFF;\n"
"	border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 300, 50))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(16)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border: none;\n"
"background-color: none;")
        self.hiragana = QPushButton(self.frame_3)
        self.hiragana.setObjectName(u"hiragana")
        self.hiragana.setGeometry(QRect(20, 70, 340, 50))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.hiragana.setFont(font1)
        self.hiragana.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hiragana.setStyleSheet(u"QPushButton {\n"
"    background-color: #1CB0F6;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border-bottom: 4px solid #1899D6;\n"
"    margin-bottom: 2px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #1FC2FF;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border-bottom: 4px solid #1899D6;\n"
"    margin-bottom: 2px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #1FC2FF;\n"
"    padding: 10px;\n"
"    border: none;\n"
"	color: #FFFFFF\n"
"}")
        self.katakana = QPushButton(self.frame_3)
        self.katakana.setObjectName(u"katakana")
        self.katakana.setGeometry(QRect(20, 140, 340, 50))
        self.katakana.setFont(font1)
        self.katakana.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.katakana.setStyleSheet(u"QPushButton {\n"
"    background-color: #1CB0F6;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border-bottom: 4px solid #1899D6;\n"
"    margin-bottom: 2px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #1FC2FF;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border-bottom: 4px solid #1899D6;\n"
"    margin-bottom: 2px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #1FC2FF;\n"
"    padding: 10px;\n"
"    border: none;\n"
"	color: #FFFFFF\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#4b4b4b;\"><b>\u8bf7\u9009\u62e9\u6a21\u5f0f</b></span></p></body></html>", None))
        self.hiragana.setText(QCoreApplication.translate("Form", u"\u5e73\u4eee\u540d", None))
        self.katakana.setText(QCoreApplication.translate("Form", u"\u7247\u4eee\u540d", None))
    # retranslateUi

