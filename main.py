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
        self.combo = 0
        self.next_action: Literal["create", "judge"] = "judge"
        self.mode: Literal["hiragana", "katakana"]

    def setupUi(self, Form):
        """初始化UI"""
        super().setupUi(Form)

        # 初始化选项按钮
        self.buttons = (
            self.option_button_1,
            self.option_button_2,
            self.option_button_3,
            self.option_button_4,
        )
        for i in range(4):
            self.buttons[i].clicked.connect(partial(self.select, i))
        self.continue_button.clicked.connect(self.next)

        # 隐藏组件
        self.judgement_label.hide()

        # 显示模式选择浮窗
        _mode_select_ui = mode_select_ui.Ui_Form()
        _mode_select_ui.setupUi(Form)

        def mode_select(mode: Literal["hiragana", "katakana"]):
            # 这是一个闭包
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
        app.continue_button.setStyleSheet(style.button_green)
        app.judgement_frame.setStyleSheet("background-color: #FFFFFF;")
        app.judgement_label.hide()
        app.answer_label.hide()
        print("creating")
        app.continue_button.setText("检查")
        self.answer = random.randint(0, 3)
        self.problem = random.sample(kana_list, 4)
        for i in range(4):
            app.buttons[i].setText(self.problem[i][self.mode])
            app.buttons[i].setChecked(False)
            app.buttons[i].setEnabled(True)
            if i == self.answer:
                app.problem_label.setText(self.problem[i]["romaji"])
                self.current_correct_kana = self.problem[i][self.mode]
        self.selected = -1
        app.continue_button.setDisabled(True)

    def select(self, order: int):
        print(f"selected {order}")
        for i in range(4):
            if i != order:
                app.buttons[i].setChecked(False)
        self.selected = order
        app.continue_button.setEnabled(True)

    def judge(self):
        print("judging")

        # 禁用按钮点击
        for i in range(4):
            app.buttons[i].setEnabled(False)

        print(f"{self.selected=}, {self.answer=}")

        # 判断答案
        if self.selected == self.answer:
            print("correct")
            app.judgement_frame.setStyleSheet("background-color: #D7FFB8;")
            app.judgement_label.setText("<span style='color:#58a700;'>正确！</span>")
            app.judgement_label.show()
            self.combo += 1
            if self.combo >= 10:
                ...  # TODO
            self.se_correct.play()
        else:
            print("incorrect")
            app.judgement_frame.setStyleSheet("background-color: #FFDFE0;")
            app.judgement_label.setText(
                "<span style='color:#ED2B2B;'>铸币吧怎么这么菜啊</span>"
            )
            app.judgement_label.show()
            app.answer_label.setText(
                f"<span style='color:#EA2B2B;'>{self.current_correct_kana}</span>"
            )
            app.answer_label.show()
            app.continue_button.setStyleSheet(style.button_red)
            self.combo = 0
            self.se_incorrect.play()
        app.combo_label.setText(f"{self.combo} Combo")
        app.continue_button.setText("继续")

    def next(self):
        match self.next_action:
            case "judge":
                self.judge()
                self.next_action = "create"
            case "create":
                self.create_problem()
                self.next_action = "judge"


application = QApplication(sys.argv)
application.styleHints().setColorScheme(Qt.ColorScheme.Light)

window = QMainWindow()
app = App()
app.setupUi(window)
window.show()

sys.exit(application.exec())
