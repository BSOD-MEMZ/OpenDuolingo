import random
import sys
from functools import partial
from typing import Literal

from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication, QMainWindow

import style
from kana_list import kana_list
from ui import main_ui, mode_select_ui


class App(main_ui.Ui_Form):
    def __init__(self):
        self.selected = -1
        self.answer = -1
        self._combo = 0
        self.next_action: Literal["create", "judge"] = "judge"
        self.mode: Literal["hiragana", "katakana"]

    def setupUi(self, Form):
        super().setupUi(Form)

        # 初始化选项按钮
        self.buttons = (
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
        )
        for i in range(4):
            self.buttons[i].clicked.connect(partial(self.select, i))
        self.continuebutton.clicked.connect(self.next)

        # 隐藏组件
        self.label_3.hide()

        # 显示模式选择浮窗
        _mode_select_ui = mode_select_ui.Ui_Form()
        _mode_select_ui.setupUi(Form)

        def mode_select(mode: Literal["hiragana", "katakana"]):
            def func():
                self.mode = mode
                self.create_problem()
                _mode_select_ui.frame_2.close()

            return func

        _mode_select_ui.hiragana.clicked.connect(mode_select("hiragana"))
        _mode_select_ui.katakana.clicked.connect(mode_select("katakana"))

        # 音效初始化
        self.se_correct = QSoundEffect(
            source=QUrl.fromLocalFile("resource/SE/correct.wav")
        )
        self.se_incorrect = QSoundEffect(
            source=QUrl.fromLocalFile("resource/SE/incorrect.wav")
        )

    def create_problem(self):
        app.continuebutton.setStyleSheet(style.button_green)
        app.frame.setStyleSheet("QFrame {\n	background-color: #FFFFFF;\n}")
        app.label_3.hide()
        app.label_4.hide()
        print("creating")
        app.continuebutton.setText("检查")
        self.answer = random.randint(0, 3)
        self.problem = random.sample(kana_list, 4)
        for i in range(4):
            app.buttons[i].setText(self.problem[i][self.mode])
            app.buttons[i].setChecked(False)
            app.buttons[i].setEnabled(True)
            if i == self.answer:
                app.label_2.setText(self.problem[i]["romaji"])
                self.current_correct_kana = self.problem[i][self.mode]
        self.selected = -1
        app.continuebutton.setDisabled(True)

    def select(self, order: int):
        print(f"selecting {order}")
        for i in range(4):
            if i != order:
                app.buttons[i].setChecked(False)
        self.selected = order
        app.continuebutton.setEnabled(True)

    def judge(self):
        print("judging")

        # 禁用按钮点击
        for i in range(4):
            app.buttons[i].setEnabled(False)

        print(f"{self.selected=}, {self.answer=}")

        # 判断答案
        if self.selected == self.answer:
            print("correct")
            app.frame.setStyleSheet("QFrame {\n	background-color: #D7FFB8;\n}")
            app.label_3.setText('<span style=" color:#58a700;">正确！</span><')
            app.label_3.show()
            self._combo += 1
            if self._combo >= 10:
                ...
            self.se_correct.play()
        else:
            print("incorrect")
            app.frame.setStyleSheet("QFrame {\n	background-color: #FFDFE0;\n}")
            app.label_3.setText(
                '<span style=" color:#ED2B2B;">铸币吧怎么这么菜啊</span>'
            )
            app.label_3.show()
            app.label_4.setText(
                f"<span style='color:#EA2B2B;'>{self.current_correct_kana}</span>"
            )
            app.label_4.show()
            app.continuebutton.setStyleSheet(style.button_red)
            self._combo = 0
            self.se_incorrect.play()
        app.combo.setText(f"{self._combo} Combo")
        app.continuebutton.setText("继续")

    def next(self):
        if self.next_action == "judge":
            self.judge()
            self.next_action = "create"
        else:
            self.create_problem()
            self.next_action = "judge"


application = QApplication(sys.argv)
application.styleHints().setColorScheme(Qt.ColorScheme.Light)

window = QMainWindow()
app = App()
app.setupUi(window)
window.show()

sys.exit(application.exec())
