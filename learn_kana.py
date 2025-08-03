import random
import sys
from enum import Enum
from functools import partial
from typing import Literal

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

import style
from ui.learn_kana import main_ui, mode_select_ui


class Kana(Enum):
    HIRA = "hiragana"  # 平假名
    KATA = "katakana"  # 片假名
    ROMA = "romaji"  # 罗马音


class KanaList:
    kana_list: list[dict[Kana, str]] = [
        {Kana.HIRA: "あ", Kana.KATA: "ア", Kana.ROMA: "a"},
        {Kana.HIRA: "い", Kana.KATA: "イ", Kana.ROMA: "i"},
        {Kana.HIRA: "う", Kana.KATA: "ウ", Kana.ROMA: "u"},
        {Kana.HIRA: "え", Kana.KATA: "エ", Kana.ROMA: "e"},
        {Kana.HIRA: "お", Kana.KATA: "オ", Kana.ROMA: "o"},
        {Kana.HIRA: "か", Kana.KATA: "カ", Kana.ROMA: "ka"},
        {Kana.HIRA: "き", Kana.KATA: "キ", Kana.ROMA: "ki"},
        {Kana.HIRA: "く", Kana.KATA: "ク", Kana.ROMA: "ku"},
        {Kana.HIRA: "け", Kana.KATA: "ケ", Kana.ROMA: "ke"},
        {Kana.HIRA: "こ", Kana.KATA: "コ", Kana.ROMA: "ko"},
        {Kana.HIRA: "さ", Kana.KATA: "サ", Kana.ROMA: "sa"},
        {Kana.HIRA: "し", Kana.KATA: "シ", Kana.ROMA: "shi"},
        {Kana.HIRA: "す", Kana.KATA: "ス", Kana.ROMA: "su"},
        {Kana.HIRA: "せ", Kana.KATA: "セ", Kana.ROMA: "se"},
        {Kana.HIRA: "そ", Kana.KATA: "ソ", Kana.ROMA: "so"},
        {Kana.HIRA: "た", Kana.KATA: "タ", Kana.ROMA: "ta"},
        {Kana.HIRA: "ち", Kana.KATA: "チ", Kana.ROMA: "chi"},
        {Kana.HIRA: "つ", Kana.KATA: "ツ", Kana.ROMA: "tsu"},
        {Kana.HIRA: "て", Kana.KATA: "テ", Kana.ROMA: "te"},
        {Kana.HIRA: "と", Kana.KATA: "ト", Kana.ROMA: "to"},
        {Kana.HIRA: "な", Kana.KATA: "ナ", Kana.ROMA: "na"},
        {Kana.HIRA: "に", Kana.KATA: "ニ", Kana.ROMA: "ni"},
        {Kana.HIRA: "ぬ", Kana.KATA: "ヌ", Kana.ROMA: "nu"},
        {Kana.HIRA: "ね", Kana.KATA: "ネ", Kana.ROMA: "ne"},
        {Kana.HIRA: "の", Kana.KATA: "ノ", Kana.ROMA: "no"},
        {Kana.HIRA: "は", Kana.KATA: "ハ", Kana.ROMA: "ha"},
        {Kana.HIRA: "ひ", Kana.KATA: "ヒ", Kana.ROMA: "hi"},
        {Kana.HIRA: "ふ", Kana.KATA: "フ", Kana.ROMA: "fu"},
        {Kana.HIRA: "へ", Kana.KATA: "ヘ", Kana.ROMA: "he"},
        {Kana.HIRA: "ほ", Kana.KATA: "ホ", Kana.ROMA: "ho"},
        {Kana.HIRA: "ま", Kana.KATA: "マ", Kana.ROMA: "ma"},
        {Kana.HIRA: "み", Kana.KATA: "ミ", Kana.ROMA: "mi"},
        {Kana.HIRA: "む", Kana.KATA: "ム", Kana.ROMA: "mu"},
        {Kana.HIRA: "め", Kana.KATA: "メ", Kana.ROMA: "me"},
        {Kana.HIRA: "も", Kana.KATA: "モ", Kana.ROMA: "mo"},
        {Kana.HIRA: "や", Kana.KATA: "ヤ", Kana.ROMA: "ya"},
        {Kana.HIRA: "ゆ", Kana.KATA: "ユ", Kana.ROMA: "yu"},
        {Kana.HIRA: "よ", Kana.KATA: "ヨ", Kana.ROMA: "yo"},
        {Kana.HIRA: "ら", Kana.KATA: "ラ", Kana.ROMA: "ra"},
        {Kana.HIRA: "り", Kana.KATA: "リ", Kana.ROMA: "ri"},
        {Kana.HIRA: "る", Kana.KATA: "ル", Kana.ROMA: "ru"},
        {Kana.HIRA: "れ", Kana.KATA: "レ", Kana.ROMA: "re"},
        {Kana.HIRA: "ろ", Kana.KATA: "ロ", Kana.ROMA: "ro"},
        {Kana.HIRA: "わ", Kana.KATA: "ワ", Kana.ROMA: "wa"},
        {Kana.HIRA: "を", Kana.KATA: "ヲ", Kana.ROMA: "wo"},
        {Kana.HIRA: "ん", Kana.KATA: "ン", Kana.ROMA: "n"},
    ]

    # 使用平假名索引
    from_hira = {k[Kana.HIRA]: k for k in kana_list}
    # 使用片假名索引
    from_kata = {k[Kana.KATA]: k for k in kana_list}
    # 使用罗马音索引
    from_roma = {k[Kana.ROMA]: k for k in kana_list}

    @classmethod
    def __class_getitem__(cls, key: str):
        # 重载 KanaList[key]
        if key in cls.from_hira:
            return cls.from_hira[key]
        elif key in cls.from_kata:
            return cls.from_kata[key]
        elif key.lower() in cls.from_roma:
            return cls.from_roma[key.lower()]
        else:
            raise IndexError(f"{key} is not found")

    @classmethod
    def pick_random(cls, number):
        """随机选取 number 个假名的键值对"""
        return random.sample(cls.kana_list, number)


class App(main_ui.Ui_Form):
    def __init__(self):
        self.selected = -1
        self.answer = -1
        self.combo = 0
        self.next_action: Literal["create", "judge"] = "judge"
        self.mode: Kana

    def setupUi(self, Form: QWidget):
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

        def mode_select(mode: Kana):
            # 这是一个闭包
            def func():
                self.mode = mode
                self.create_problem()
                _mode_select_ui.frame_2.close()

            return func

        _mode_select_ui.hiragana.clicked.connect(mode_select(Kana.HIRA))
        _mode_select_ui.katakana.clicked.connect(mode_select(Kana.KATA))

        # 音效初始化
        self.se_correct = QSoundEffect(source=QUrl.fromLocalFile("resources/SE/correct.wav"))
        self.se_incorrect = QSoundEffect(source=QUrl.fromLocalFile("resources/SE/incorrect.wav"))

        # 字体初始化
        families = QFontDatabase.applicationFontFamilies(
            QFontDatabase.addApplicationFont("resources/fonts/DINRound.otf")
        )
        duo_font = f"{families[0]}, " if families else ""

        self.font = QFont(f"{duo_font}Microsoft YaHei UI, sans-serif")
        Form.setFont(self.font)

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
                self.problem_label.setText(problems[i][Kana.ROMA])
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
            self.judgement_label.setText("<span style='color:#ED2B2B;'>铸币吧怎么这么菜啊</span>")
            self.judgement_label.show()
            self.answer_label.setText(f"<span style='color:#EA2B2B;'>{self.answer_text}</span>")
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


if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.styleHints().setColorScheme(Qt.ColorScheme.Light)

    window = QMainWindow()
    window.setWindowTitle("Openlingo")
    window.setFixedSize(580, 440)

    app = App()
    app.setupUi(window)

    window.show()

    sys.exit(application.exec())
