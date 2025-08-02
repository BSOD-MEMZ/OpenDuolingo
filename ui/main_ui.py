# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        Form.resize(584, 445)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        Form.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        Form.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 120, 120, 130))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(36)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #F7F7F7;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #88D8FF;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}")
        self.pushButton.setCheckable(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 300, 40))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 100, 50))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic"])
        font3.setPointSize(36)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.combo = QLabel(Form)
        self.combo.setObjectName(u"combo")
        self.combo.setGeometry(QRect(460, 20, 140, 40))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic"])
        font4.setPointSize(18)
        font4.setBold(False)
        self.combo.setFont(font4)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 340, 581, 101))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(10, 10, 340, 40))
        self.label_3.setFont(font2)
        self.continuebutton = QPushButton(self.frame)
        self.continuebutton.setObjectName(u"continuebutton")
        self.continuebutton.setGeometry(QRect(410, 30, 141, 51))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.continuebutton.setFont(font5)
        self.continuebutton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.continuebutton.setStyleSheet(u"QPushButton {\n"
"    background-color: #58CC02;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border-bottom: 4px solid #58A700;\n"
"    margin-bottom: 2px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #61E002;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border-bottom: 4px solid #58A700;\n"
"    margin-bottom: 2px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #61E002;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	color: #FFFFFF\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 16px;\n"
"	border: none;\n"
"	color: #AFAFAF;\n"
"}\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(10, 45, 370, 40))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei UI"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.label_4.setFont(font6)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 120, 120, 130))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #F7F7F7;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #88D8FF;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 120, 120, 130))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #F7F7F7;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #88D8FF;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}")
        self.pushButton_3.setCheckable(True)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(440, 120, 120, 130))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #F7F7F7;\n"
"    border: 2px solid #E5E5E5;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #E5E5E5;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: #D3F4FF;\n"
"    border: 2px solid #88D8FF;\n"
"    padding: 10px;\n"
"    border-radius: 12px;\n"
"	border-bottom: 4px solid #88D8FF;\n"
"    margin-bottom: 2px;\n"
"	color: #1899D6;\n"
"}")
        self.pushButton_4.setCheckable(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"OpenDuolingo", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u3042", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#3c3c3c;\"><b>\u9009\u62e9\u6b63\u786e\u7684\u5047\u540d</b></span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"a", None))
        self.combo.setText(QCoreApplication.translate("Form", u"0 Combo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#58a700;\">\u771f\u68d2\uff01</span></p></body></html>", None))
        self.continuebutton.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#EA2B2B;\">fuck</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u3042", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u3042", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u3042", None))
    # retranslateUi

