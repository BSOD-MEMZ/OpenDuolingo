import random
import sys
from typing import Literal

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

from ui import challenge


class KanaList:
    kana_list: list[dict[Literal["hira", "kata", "roma"], str]] = [
        {"hira": "あ", "kata": "ア", "roma": "a"},
        {"hira": "い", "kata": "イ", "roma": "i"},
        {"hira": "う", "kata": "ウ", "roma": "u"},
        {"hira": "え", "kata": "エ", "roma": "e"},
        {"hira": "お", "kata": "オ", "roma": "o"},
        {"hira": "か", "kata": "カ", "roma": "ka"},
        {"hira": "き", "kata": "キ", "roma": "ki"},
        {"hira": "く", "kata": "ク", "roma": "ku"},
        {"hira": "け", "kata": "ケ", "roma": "ke"},
        {"hira": "こ", "kata": "コ", "roma": "ko"},
        {"hira": "さ", "kata": "サ", "roma": "sa"},
        {"hira": "し", "kata": "シ", "roma": "shi"},
        {"hira": "す", "kata": "ス", "roma": "su"},
        {"hira": "せ", "kata": "セ", "roma": "se"},
        {"hira": "そ", "kata": "ソ", "roma": "so"},
        {"hira": "た", "kata": "タ", "roma": "ta"},
        {"hira": "ち", "kata": "チ", "roma": "chi"},
        {"hira": "つ", "kata": "ツ", "roma": "tsu"},
        {"hira": "て", "kata": "テ", "roma": "te"},
        {"hira": "と", "kata": "ト", "roma": "to"},
        {"hira": "な", "kata": "ナ", "roma": "na"},
        {"hira": "に", "kata": "ニ", "roma": "ni"},
        {"hira": "ぬ", "kata": "ヌ", "roma": "nu"},
        {"hira": "ね", "kata": "ネ", "roma": "ne"},
        {"hira": "の", "kata": "ノ", "roma": "no"},
        {"hira": "は", "kata": "ハ", "roma": "ha"},
        {"hira": "ひ", "kata": "ヒ", "roma": "hi"},
        {"hira": "ふ", "kata": "フ", "roma": "fu"},
        {"hira": "へ", "kata": "ヘ", "roma": "he"},
        {"hira": "ほ", "kata": "ホ", "roma": "ho"},
        {"hira": "ま", "kata": "マ", "roma": "ma"},
        {"hira": "み", "kata": "ミ", "roma": "mi"},
        {"hira": "む", "kata": "ム", "roma": "mu"},
        {"hira": "め", "kata": "メ", "roma": "me"},
        {"hira": "も", "kata": "モ", "roma": "mo"},
        {"hira": "や", "kata": "ヤ", "roma": "ya"},
        {"hira": "ゆ", "kata": "ユ", "roma": "yu"},
        {"hira": "よ", "kata": "ヨ", "roma": "yo"},
        {"hira": "ら", "kata": "ラ", "roma": "ra"},
        {"hira": "り", "kata": "リ", "roma": "ri"},
        {"hira": "る", "kata": "ル", "roma": "ru"},
        {"hira": "れ", "kata": "レ", "roma": "re"},
        {"hira": "ろ", "kata": "ロ", "roma": "ro"},
        {"hira": "わ", "kata": "ワ", "roma": "wa"},
        {"hira": "を", "kata": "ヲ", "roma": "wo"},
        {"hira": "ん", "kata": "ン", "roma": "n"},
    ]

    # 使用平假名索引
    from_hira = {k["hira"]: k for k in kana_list}
    # 使用片假名索引
    from_kata = {k["kata"]: k for k in kana_list}
    # 使用罗马音索引
    from_roma = {k["roma"]: k for k in kana_list}

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


class App:
    def __init__(self, parent):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle("模式选择")
        msg_box.setText("请选择模式")

        button_hira = QPushButton("平假名")
        button_kata = QPushButton("片假名")

        msg_box.addButton(button_hira, QMessageBox.ButtonRole.AcceptRole)
        msg_box.addButton(button_kata, QMessageBox.ButtonRole.RejectRole)

        msg_box.exec()

        mode = "kata" if msg_box.clickedButton() == button_kata else "hira"

        self.setupUi(mode)

    def setupUi(self, mode: Literal["hira", "kata"], number=20):
        data: list[challenge.ChallengeData] = []
        for i in range(number):
            options = [k[mode] for k in KanaList.pick_random(4)]
            answer = random.randint(0, 3)
            data.append(
                challenge.ChallengeData(
                    "single-char", f"选择 “{KanaList[options[answer]]['roma']}” 对应的字符", options, answer
                )
            )
        self.ui = challenge.ChallengeUI(data)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.styleHints().setColorScheme(Qt.ColorScheme.Light)

    families = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(r"resources\fonts\DINRound.otf"))
    font = QFont(f"{f'{families[0]}, ' if families else ''}Microsoft YaHei UI, sans-serif")
    application.setFont(font)

    window = QMainWindow()
    window.setWindowTitle("Openlingo")
    window.resize(900, 690)

    palette = window.palette()
    palette.setColor(window.backgroundRole(), "#FFFFFF")
    window.setPalette(palette)

    app = App(window)

    app.ui.setStyleSheet("outline: none;")
    window.setCentralWidget(app.ui)

    window.show()

    sys.exit(application.exec())
