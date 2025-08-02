import random
import sys
from functools import partial
from typing import Literal

from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication, QMainWindow

import style
from kana_list import KanaList
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
            self.buttons[i].clicked.connect(partial(self.on_select, i))
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
        """出题"""
        self.continue_button.setStyleSheet(style.button_green)
        self.judgement_frame.setStyleSheet("background-color: #FFFFFF;")
        self.judgement_label.hide()
        self.answer_label.hide()

        print("creating")
        self.answer = random.randint(0, 3)
        problems = KanaList.pick_random(4)
        for i in range(4):
            button = self.buttons[i]
            button.setText(problems[i][self.mode])
            button.setChecked(False)
            button.setEnabled(True)
            if i == self.answer:
                self.problem_label.setText(problems[i]["romaji"])
                self.answer_text = problems[i][self.mode]

        self.selected = -1
        self.continue_button.setText("检查")
        self.continue_button.setDisabled(True)

    def on_select(self, order: int):
        """按钮选中事件"""
        print(f"selected {order}")
        for i in range(4):
            if i != order:
                self.buttons[i].setChecked(False)
        self.selected = order
        self.continue_button.setEnabled(True)

    def judge(self):
        """判题"""
        print("judging")

        # 禁用按钮点击
        for i in range(4):
            self.buttons[i].setEnabled(False)

        print(f"{self.selected=}, {self.answer=}")

        # 判断答案
        if self.selected == self.answer:
            print("correct")
            self.judgement_frame.setStyleSheet("background-color: #D7FFB8;")
            self.judgement_label.setText("<span style='color:#58a700;'>正确！</span>")
            self.judgement_label.show()
            self.combo += 1
            if self.combo >= 10:
                ...  # TODO
            self.se_correct.play()
        else:
            print("incorrect")
            self.judgement_frame.setStyleSheet("background-color: #FFDFE0;")
            self.judgement_label.setText(
                "<span style='color:#ED2B2B;'>铸币吧怎么这么菜啊</span>"
            )
            self.judgement_label.show()
            self.answer_label.setText(
                f"<span style='color:#EA2B2B;'>{self.answer_text}</span>"
            )
            self.answer_label.show()
            self.continue_button.setStyleSheet(style.button_red)
            self.combo = 0
            self.se_incorrect.play()
        self.combo_label.setText(f"{self.combo} Combo")
        self.continue_button.setText("继续")

    def next(self):
        """下一步操作，适用于 continue_button"""
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
window.setWindowTitle("Openlingo")
window.setFixedSize(580, 440)

app = App()
app.setupUi(window)

window.show()

sys.exit(application.exec())
