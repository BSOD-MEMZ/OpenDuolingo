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
        self.option_button_1 = QPushButton(Form)
        self.option_button_1.setObjectName(u"option_button_1")
        self.option_button_1.setGeometry(QRect(20, 120, 120, 130))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(36)
        self.option_button_1.setFont(font1)
        self.option_button_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.option_button_1.setStyleSheet(u"QPushButton {\n"
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
        self.option_button_1.setCheckable(True)
        self.hint_labell = QLabel(Form)
        self.hint_labell.setObjectName(u"hint_labell")
        self.hint_labell.setGeometry(QRect(20, 10, 300, 40))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.hint_labell.setFont(font2)
        self.problem_label = QLabel(Form)
        self.problem_label.setObjectName(u"problem_label")
        self.problem_label.setGeometry(QRect(20, 60, 100, 50))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic"])
        font3.setPointSize(36)
        font3.setBold(True)
        self.problem_label.setFont(font3)
        self.combo_label = QLabel(Form)
        self.combo_label.setObjectName(u"combo_label")
        self.combo_label.setGeometry(QRect(460, 20, 140, 40))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic"])
        font4.setPointSize(18)
        font4.setBold(False)
        self.combo_label.setFont(font4)
        self.judgement_frame = QFrame(Form)
        self.judgement_frame.setObjectName(u"judgement_frame")
        self.judgement_frame.setGeometry(QRect(0, 340, 581, 101))
        self.judgement_frame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"}")
        self.judgement_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.judgement_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.judgement_label = QLabel(self.judgement_frame)
        self.judgement_label.setObjectName(u"judgement_label")
        self.judgement_label.setEnabled(True)
        self.judgement_label.setGeometry(QRect(10, 10, 340, 40))
        self.judgement_label.setFont(font2)
        self.continue_button = QPushButton(self.judgement_frame)
        self.continue_button.setObjectName(u"continue_button")
        self.continue_button.setGeometry(QRect(410, 30, 141, 51))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.continue_button.setFont(font5)
        self.continue_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.continue_button.setStyleSheet(u"QPushButton {\n"
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
        self.answer_label = QLabel(self.judgement_frame)
        self.answer_label.setObjectName(u"answer_label")
        self.answer_label.setEnabled(True)
        self.answer_label.setGeometry(QRect(10, 45, 370, 40))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei UI"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.answer_label.setFont(font6)
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.option_button_2 = QPushButton(Form)
        self.option_button_2.setObjectName(u"option_button_2")
        self.option_button_2.setGeometry(QRect(160, 120, 120, 130))
        self.option_button_2.setFont(font1)
        self.option_button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.option_button_2.setStyleSheet(u"QPushButton {\n"
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
        self.option_button_2.setCheckable(True)
        self.option_button_3 = QPushButton(Form)
        self.option_button_3.setObjectName(u"option_button_3")
        self.option_button_3.setGeometry(QRect(300, 120, 120, 130))
        self.option_button_3.setFont(font1)
        self.option_button_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.option_button_3.setStyleSheet(u"QPushButton {\n"
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
        self.option_button_3.setCheckable(True)
        self.option_button_4 = QPushButton(Form)
        self.option_button_4.setObjectName(u"option_button_4")
        self.option_button_4.setGeometry(QRect(440, 120, 120, 130))
        self.option_button_4.setFont(font1)
        self.option_button_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.option_button_4.setStyleSheet(u"QPushButton {\n"
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
        self.option_button_4.setCheckable(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"OpenDuolingo", None))
        self.option_button_1.setText(QCoreApplication.translate("Form", u"\u3042", None))
        self.hint_labell.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#3c3c3c;\"><b>\u9009\u62e9\u6b63\u786e\u7684\u5047\u540d</b></span></p></body></html>", None))
        self.problem_label.setText(QCoreApplication.translate("Form", u"a", None))
        self.combo_label.setText(QCoreApplication.translate("Form", u"0 Combo", None))
        self.judgement_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#58a700;\">\u771f\u68d2\uff01</span></p></body></html>", None))
        self.continue_button.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5", None))
        self.answer_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#EA2B2B;\">fuck</span></p></body></html>", None))
        self.option_button_2.setText(QCoreApplication.translate("Form", u"\u3042", None))
        self.option_button_3.setText(QCoreApplication.translate("Form", u"\u3042", None))
        self.option_button_4.setText(QCoreApplication.translate("Form", u"\u3042", None))
    # retranslateUi

