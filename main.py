import random
import sys
import winsound
from functools import partial
from typing import Literal

from PySide6.QtWidgets import QApplication, QWidget

import style
from kana_list import kana_list
from main_ui import Ui_Form

selected = -1
answer = -1
combo = 0
hiragana = True
next_action: Literal["create", "judge"] = "judge"


def createProblem():
    ui.continuebutton.setStyleSheet(style.button_green)
    global problem, current_correct_kana
    ui.frame.setStyleSheet("QFrame {\n	background-color: #FFFFFF;\n}")
    ui.label_3.hide()
    ui.label_4.hide()
    print("creating")
    ui.continuebutton.setText("检查")
    global selected, answer
    answer = random.randint(0, 3)
    problem = random.sample(kana_list, 4)
    for i in range(4):
        if hiragana:
            ui.buttons[i].setText(problem[i]["hiragana"])
        else:
            ui.buttons[i].setText(problem[i]["katakana"])
        ui.buttons[i].setChecked(False)
        ui.buttons[i].setEnabled(True)
        if i == answer:
            ui.label_2.setText(problem[i]["romaji"])
            if hiragana:
                current_correct_kana = problem[i]["hiragana"]
            else:
                current_correct_kana = problem[i]["katakana"]
    selected = -1
    ui.continuebutton.setDisabled(True)


def select(order: int):
    print(f"selecting {order}")
    global selected
    for i in range(4):
        if i != order:
            ui.buttons[i].setChecked(False)
    selected = order
    ui.continuebutton.setEnabled(True)


def judge():
    global problem
    print("judging")
    global selected, answer, combo
    for i in range(4):
        ui.buttons[i].setEnabled(False)
    print(f"选择的选项: {selected}, 正确答案位置: {answer}")
    if selected == answer:
        print("correct")
        ui.frame.setStyleSheet("QFrame {\n	background-color: #D7FFB8;\n}")
        ui.label_3.setText(
            '<html><head/><body><p><span style=" color:#58a700;">正确！</span></p></body></html>'
        )
        ui.label_3.show()
        combo += 1
        if combo >= 10:
            ...
        winsound.PlaySound("resource/seikai.wav", winsound.SND_ASYNC)
    else:
        print("incorrect")
        ui.frame.setStyleSheet("QFrame {\n	background-color: #FFDFE0;\n}")
        ui.label_3.setText(
            '<html><head/><body><p><span style=" color:#ED2B2B;">铸币吧怎么这么菜啊</span></p></body></html>'
        )
        ui.label_3.show()
        ui.label_4.setText(
            '<html><head/><body><p><span style=" color:#EA2B2B;">'
            + current_correct_kana
            + "</span></p></body></html>"
        )
        ui.label_4.show()
        ui.continuebutton.setStyleSheet(style.button_red)
        combo = 0
        winsound.PlaySound("resource/fuseikai.wav", winsound.SND_ASYNC)
    ui.combo.setText(f"{combo} Combo")
    ui.continuebutton.setText("继续")


def next():
    global next_action
    if next_action == "judge":
        judge()
        next_action = "create"
    else:
        createProblem()
        next_action = "judge"


class AppUI(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

        self.buttons = (
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
        )

        for i in range(4):
            self.buttons[i].clicked.connect(partial(select, i))
        self.continuebutton.clicked.connect(next)


def startkatakana():
    global hiragana
    hiragana = False
    createProblem()
    ui.frame_2.hide()


app = QApplication(sys.argv)
w = QWidget()
ui = AppUI()
ui.setupUi(w)
w.show()
ui.label_3.hide()
createProblem()
ui.hiragana.clicked.connect(lambda: ui.frame_2.hide())
ui.katakana.clicked.connect(lambda: startkatakana())
sys.exit(app.exec())
