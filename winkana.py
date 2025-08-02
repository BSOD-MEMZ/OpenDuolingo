import random
import sys
import winsound
from functools import partial
from typing import List, Literal

from PyQt6.QtWidgets import QApplication, QWidget

from winkana_ui import Ui_Form

kana_list: List[dict[Literal["hiragana", "katakana", "romaji"], str]] = [
    {"hiragana": "あ", "katakana": "ア", "romaji": "a"},
    {"hiragana": "い", "katakana": "イ", "romaji": "i"},
    {"hiragana": "う", "katakana": "ウ", "romaji": "u"},
    {"hiragana": "え", "katakana": "エ", "romaji": "e"},
    {"hiragana": "お", "katakana": "オ", "romaji": "o"},
    {"hiragana": "か", "katakana": "カ", "romaji": "ka"},
    {"hiragana": "き", "katakana": "キ", "romaji": "ki"},
    {"hiragana": "く", "katakana": "ク", "romaji": "ku"},
    {"hiragana": "け", "katakana": "ケ", "romaji": "ke"},
    {"hiragana": "こ", "katakana": "コ", "romaji": "ko"},
    {"hiragana": "さ", "katakana": "サ", "romaji": "sa"},
    {"hiragana": "し", "katakana": "シ", "romaji": "shi"},
    {"hiragana": "す", "katakana": "ス", "romaji": "su"},
    {"hiragana": "せ", "katakana": "セ", "romaji": "se"},
    {"hiragana": "そ", "katakana": "ソ", "romaji": "so"},
    {"hiragana": "た", "katakana": "タ", "romaji": "ta"},
    {"hiragana": "ち", "katakana": "チ", "romaji": "chi"},
    {"hiragana": "つ", "katakana": "ツ", "romaji": "tsu"},
    {"hiragana": "て", "katakana": "テ", "romaji": "te"},
    {"hiragana": "と", "katakana": "ト", "romaji": "to"},
    {"hiragana": "な", "katakana": "ナ", "romaji": "na"},
    {"hiragana": "に", "katakana": "ニ", "romaji": "ni"},
    {"hiragana": "ぬ", "katakana": "ヌ", "romaji": "nu"},
    {"hiragana": "ね", "katakana": "ネ", "romaji": "ne"},
    {"hiragana": "の", "katakana": "ノ", "romaji": "no"},
    {"hiragana": "は", "katakana": "ハ", "romaji": "ha"},
    {"hiragana": "ひ", "katakana": "ヒ", "romaji": "hi"},
    {"hiragana": "ふ", "katakana": "フ", "romaji": "fu"},
    {"hiragana": "へ", "katakana": "ヘ", "romaji": "he"},
    {"hiragana": "ほ", "katakana": "ホ", "romaji": "ho"},
    {"hiragana": "ま", "katakana": "マ", "romaji": "ma"},
    {"hiragana": "み", "katakana": "ミ", "romaji": "mi"},
    {"hiragana": "む", "katakana": "ム", "romaji": "mu"},
    {"hiragana": "め", "katakana": "メ", "romaji": "me"},
    {"hiragana": "も", "katakana": "モ", "romaji": "mo"},
    {"hiragana": "や", "katakana": "ヤ", "romaji": "ya"},
    {"hiragana": "ゆ", "katakana": "ユ", "romaji": "yu"},
    {"hiragana": "よ", "katakana": "ヨ", "romaji": "yo"},
    {"hiragana": "ら", "katakana": "ラ", "romaji": "ra"},
    {"hiragana": "り", "katakana": "リ", "romaji": "ri"},
    {"hiragana": "る", "katakana": "ル", "romaji": "ru"},
    {"hiragana": "れ", "katakana": "レ", "romaji": "re"},
    {"hiragana": "ろ", "katakana": "ロ", "romaji": "ro"},
    {"hiragana": "わ", "katakana": "ワ", "romaji": "wa"},
    {"hiragana": "を", "katakana": "ヲ", "romaji": "wo"},
    {"hiragana": "ん", "katakana": "ン", "romaji": "n"},
]
hira_to = {k["hiragana"]: k for k in kana_list}
kata_to = {k["katakana"]: k for k in kana_list}
roma_to = {k["romaji"]: k for k in kana_list}

selected = -1
answer = -1
combo = 0
hiragana = True
next_action: Literal["create", "judge"] = "judge"


def createProblem():
    ui.continuebutton.setStyleSheet(
        "QPushButton {\n"
        "    background-color: #58CC02;\n"
        "    padding: 10px;\n"
        "    border-radius: 16px;\n"
        "    border-bottom: 4px solid #58A700;\n"
        "    margin-bottom: 2px;\n"
        "    color: #FFFFFF\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: #61E002;\n"
        "    padding: 10px;\n"
        "    border-radius: 16px;\n"
        "    border-bottom: 4px solid #58A700;\n"
        "    margin-bottom: 2px;\n"
        "    color: #FFFFFF\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: #61E002;\n"
        "    padding: 10px;\n"
        "    border-radius: 16px;\n"
        "    color: #FFFFFF\n"
        "}\n"
        "QPushButton:disabled{\n"
        "    background-color: #E5E5E5;\n"
        "    padding: 10px;\n"
        "    border-radius: 16px;\n"
        "    border: none;\n"
        "    color: #AFAFAF;\n"
        "}\n"
        ""
    )
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
        ui.buttons[i].setStyleSheet(
            "QPushButton {\n"
            "    background-color: #FFFFFF;\n"
            "    border: 2px solid #E5E5E5;\n"
            "    padding: 10px;\n"
            "    border-radius: 12px;\n"
            "    border-bottom: 4px solid #E5E5E5;\n"
            "    margin-bottom: 2px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    background-color: #F7F7F7;\n"
            "    border: 2px solid #E5E5E5;\n"
            "    padding: 10px;\n"
            "    border-radius: 12px;\n"
            "    border-bottom: 4px solid #E5E5E5;\n"
            "    margin-bottom: 2px;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    background-color: #D3F4FF;\n"
            "    border: 2px solid #88D8FF;\n"
            "    padding: 10px;\n"
            "    border-radius: 12px;\n"
            "    margin-bottom: 2px;\n"
            "    color: #1899D6;\n"
            "}\n"
            "QPushButton:checked{\n"
            "    background-color: #D3F4FF;\n"
            "    border: 2px solid #88D8FF;\n"
            "    padding: 10px;\n"
            "    border-radius: 12px;\n"
            "    border-bottom: 4px solid #88D8FF;\n"
            "    margin-bottom: 2px;\n"
            "    color: #1899D6;\n"
            "}"
        )
        if i == answer:
            ui.label_2.setText(problem[i]["romaji"])
            if hiragana:
                current_correct_kana = problem[i]["hiragana"]
            else:
                current_correct_kana = problem[i]["katakana"]
    selected = -1
    ui.continuebutton.setDisabled(True)


def select(order: int):
    print(f"seleting {order}")
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
        winsound.PlaySound("seikai.wav", winsound.SND_ASYNC)
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
        ui.continuebutton.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #FF4B4B;\n"
            "    padding: 10px;\n"
            "    border-radius: 16px;\n"
            "    border-bottom: 4px solid #EA2B2B;\n"
            "    margin-bottom: 2px;\n"
            "    color: #FFFFFF\n"
            "}\n"
            "QPushButton:hover{\n"
            "    background-color: #FF5252;\n"
            "    padding: 10px;\n"
            "    border-radius: 16px;\n"
            "    border-bottom: 4px solid #EA2B2B;\n"
            "    margin-bottom: 2px;\n"
            "    color: #FFFFFF\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    background-color: #FF5252;\n"
            "    padding: 10px;\n"
            "    border-radius: 16px;\n"
            "    color: #FFFFFF\n"
            "}\n"
            "QPushButton:disabled{\n"
            "    background-color: #E5E5E5;\n"
            "    padding: 10px;\n"
            "    border-radius: 16px;\n"
            "    border: none;\n"
            "    color: #AFAFAF;\n"
            "}\n"
            ""
        )
        combo = 0
        winsound.PlaySound("fuseikai.wav", winsound.SND_ASYNC)
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
