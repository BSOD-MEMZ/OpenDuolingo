import json
import time
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Self

from PySide6.QtCore import QEasingCurve, QSize, Qt, QTimer, QUrl, Signal
from PySide6.QtGui import QColor, QFont, QFontDatabase, QPainter, QPaintEvent, QPixmap
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

import style


class MetaQObjectABC(ABCMeta, type(QWidget)):
    """兼容元类"""

    pass


class AbstractChallenge(QWidget, metaclass=MetaQObjectABC):
    """题目的抽象基类，所有题目必须继承此类并实现声明的方法"""

    # 必须在答案可用时发出该信号
    optionSelected = Signal(bool)

    @abstractmethod
    def check_answer(self) -> tuple[bool, str]:
        """检查答案

        Returns:
            tuple[bool, str]: 二元组，分别为题目正误和正确答案
        """
        ...


class SingleChoice(AbstractChallenge):
    """单项选择"""

    def __init__(self, options: list[str], answer: int):
        super().__init__()

        self.setStyleSheet(style.button_option)

        # 选项
        self.option_texts = options
        self.option_buttons: list[QPushButton] = []

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # 单选

        layout = QGridLayout(self)
        layout.setHorizontalSpacing(8)

        # 遍历题目
        for i, text in enumerate(options):
            button = QPushButton(text)
            button.setMaximumSize(144, 220)
            button.setCheckable(True)

            self.option_buttons.append(button)
            self.button_group.addButton(button, i)
            layout.addWidget(button, 0, i)

        self.button_group.idClicked.connect(self.on_option_selected)

        # 答案
        assert answer <= len(options)
        self.answer = answer

    def on_option_selected(self, id: int):
        """选中事件"""
        print(f"Option {self.option_texts[id]} ({id=}) is selected")
        self.selected = id
        self.optionSelected.emit(True)

    def check_answer(self):
        """检查答案"""
        print(f"Checking... (selected: {self.selected}, answer: {self.answer}")
        result = self.selected == self.answer
        if result:
            self.option_buttons[self.selected].setProperty("correct", "true")
            print("True")
        else:
            print("False")
        for button in self.option_buttons:
            button.setEnabled(False)
        return result, self.option_texts[self.answer]


@dataclass
class ChallengeData:
    """题目数据"""

    type: Literal["single"]
    question: str
    options: list[str]
    answer: int

    @classmethod
    def from_json(cls, path: str | Path) -> list[Self]:
        """从json解析题目数据"""
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw = json.load(f)
            return [cls(**item) for item in raw]
        except Exception as e:
            raise ValueError(f"Error phasing data: {e}") from e

    def create_challenge(self) -> AbstractChallenge:
        match self.type:
            case "single":
                return SingleChoice(options=self.options, answer=self.answer)
            case _:
                raise TypeError(f"Unknown challenge type {self.type}")


class AlignedContainer(QWidget):
    """自动对齐的容器"""

    def __init__(
        self,
        widget: QWidget,
        layout: type[QLayout] = QHBoxLayout,
        align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        no_margin: bool = True,
    ):
        super().__init__()
        _layout = layout(self)
        _layout.setAlignment(align)
        if no_margin:
            _layout.setContentsMargins(0, 0, 0, 0)

        _layout.addWidget(widget)


class AnimatedProgressBar(QProgressBar):
    """平滑切换的进度条"""

    def __init__(self, parent=None, duration_ms=500, easing_curve=QEasingCurve.OutCubic, precision=1000):
        super().__init__(parent)
        self._duration = duration_ms
        self._easing = QEasingCurve(easing_curve)
        self._precision = precision

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_animation)
        self._interval = 16  # ~60FPS

        self._start_time = 0.0
        self._start_value_internal = 0
        self._target_value_internal = 0

        self._min = 0
        self._max = 100

    def setRange(self, minimum: int, maximum: int):
        self._min = minimum
        self._max = maximum
        super().setRange(minimum * self._precision, maximum * self._precision)

    def setValue(self, value: int):
        self.set_animated_value(value)

    def _set_internal_value(self, internal_val: int):
        super().setValue(internal_val)

    def value(self) -> int:
        return super().value() // self._precision

    def set_animated_value(self, value: int):
        value = max(self._min, min(self._max, value))

        if self._timer.isActive():
            self._timer.stop()

        self._start_time = time.time()
        self._start_value_internal = super().value()
        self._target_value_internal = value * self._precision

        self._timer.start(self._interval)

    def _update_animation(self):
        elapsed_ms = (time.time() - self._start_time) * 1000
        progress = min(1.0, elapsed_ms / self._duration)
        eased_progress = self._easing.valueForProgress(progress)
        new_val = (
            self._start_value_internal + (self._target_value_internal - self._start_value_internal) * eased_progress
        )

        self._set_internal_value(int(round(new_val)))

        if progress >= 1.0:
            self._timer.stop()


class RoundIconWidget(QWidget):
    """圆底图标"""

    def __init__(self, icon_path: str, diameter: int = 80, parent=None):
        super().__init__(parent)
        self.diameter = diameter
        self.setFixedSize(QSize(diameter, diameter))
        self.icon = QPixmap(icon_path).scaled(diameter // 2, diameter // 2, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 画白色圆形背景
        painter.setBrush(QColor("white"))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.diameter, self.diameter)

        # 画中心图标
        icon_x = (self.width() - self.icon.width()) // 2
        icon_y = (self.height() - self.icon.height()) // 2
        painter.drawPixmap(icon_x, icon_y, self.icon)


class AnswerResult(QWidget):
    """作答结果展示组件"""

    def __init__(self, is_correct: bool, title: str, detail: str | None = None):
        super().__init__()
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        # 图标
        self.icon = RoundIconWidget(f"resources/icons/{'correct' if is_correct else 'incorrect'}.png")

        # 信息区
        self.info_area = QWidget()
        self.info_area.setFixedWidth(320)
        info_layout = QVBoxLayout(self.info_area)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(16)

        ## 信息内容
        self.info_content = QWidget()
        self.setStyleSheet("QLabel { padding: 0; }")
        content_layout = QVBoxLayout(self.info_content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        ### 标题
        self.info_title = QLabel(title)
        self.info_title.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.info_title.setFixedHeight(30)
        content_layout.addWidget(self.info_title)
        if detail:
            self.info_detail = QLabel(detail)
            self.info_detail.setStyleSheet("font-size: 17px; font-weight: 500;")
            self.info_detail.setFixedHeight(26)
            content_layout.addWidget(self.info_detail)
        else:
            content_layout.addWidget(QWidget())

        ## 报告按钮
        self.report_button = QLabel("HAVE OBJECTION?")
        self.report_button.setCursor(Qt.PointingHandCursor)
        self.report_button.setStyleSheet(f"color: {'#7EC137' if is_correct else '#F06161'}; font-size: 14px;")

        info_layout.addWidget(self.info_content)
        info_layout.addWidget(self.report_button)

        layout.addWidget(self.icon, 0, 0)
        layout.addWidget(self.info_area, 0, 1)
        layout.addWidget(QWidget(), 0, 2)


class ChallengeUI(QWidget):
    """通用答题界面"""

    def __init__(self, challenges: list[ChallengeData]):
        super().__init__()

        # 题目
        self.challenges = challenges
        self.challenge_index = 0

        # 样式
        self.setStyleSheet("outline: none;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        ## 状态区
        self.status_area = QWidget()
        self.status_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.status_area.setMaximumWidth(1080)
        self.status_area.setFixedHeight(32)

        self.status_container = AlignedContainer(
            self.status_area, QHBoxLayout, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter
        )
        self.status_container.setContentsMargins(40, 0, 40, 18)
        self.status_container.setFixedHeight(100)
        layout.addWidget(self.status_container)

        ## 题目区
        self.challenge_area = QWidget()
        self.challenge_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.challenge_area.setMaximumSize(600, 450)
        self.challenge_area.setMinimumHeight(400)

        self.challenge_container = AlignedContainer(self.challenge_area, QHBoxLayout, Qt.AlignmentFlag.AlignHCenter)
        self.challenge_container.setMinimumWidth(700)

        layout.addWidget(self.challenge_container)

        ## 作答区
        self.judgment_area = QFrame()
        self.judgment_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.judgment_area.setMaximumWidth(1000)

        self.judgment_container = AlignedContainer(self.judgment_area, QHBoxLayout, Qt.AlignmentFlag.AlignHCenter)
        self.judgment_container.setFixedHeight(140)
        self.judgment_container.setStyleSheet("border-top: 2px solid #E5E5E5")

        layout.addWidget(self.judgment_container)

        # 内部
        ## 状态区
        self.status_layout = QGridLayout(self.status_area)
        self.status_layout.setContentsMargins(0, 0, 0, 0)
        self.status_layout.setHorizontalSpacing(24)

        ### 退出按钮
        self.exit_button = QPushButton()
        self.exit_button.setIcon(QPixmap("resources/icons/exit.png"))
        self.exit_button.setFixedSize(32, 32)
        self.exit_button.setStyleSheet("background: none; border: none; qproperty-iconSize: 20px 20px;")
        self.exit_button.setCursor(Qt.PointingHandCursor)

        ### 进度条
        self.progress_bar = AnimatedProgressBar()
        self.progress_bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.progress_bar.setFixedHeight(16)

        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet(style.progress_bar)
        self.progress_bar.setRange(0, len(self.challenges))
        self.progress_bar.setValue(0)

        ### 红心数
        self.heart_count_display = QWidget()
        self.heart_count_display.setFixedWidth(50)

        self.status_layout.addWidget(self.exit_button, 0, 0)
        self.status_layout.addWidget(self.progress_bar, 0, 1)
        self.status_layout.addWidget(self.heart_count_display, 0, 2)

        ## 题目区
        self.challenge_layout = QVBoxLayout(self.challenge_area)
        self.challenge_layout.setContentsMargins(0, 0, 0, 0)
        self.challenge_layout.setSpacing(24)

        self.update_challenge()

        ## 作答区
        self.judgment_area.setStyleSheet("QFrame { padding: 0px 40px; }")
        self.judgment_layout = QGridLayout(self.judgment_area)
        self.judgment_layout.setContentsMargins(0, 0, 0, 0)
        self.judgment_layout.setHorizontalSpacing(16)

        for i in range(5):
            self.judgment_layout.setColumnStretch(i, 1)

        ### 左侧按钮（跳过）
        self.judge_button_left = QPushButton("跳过")
        self.judge_button_left.setFixedSize(150, 48)
        self.judge_button_left.setCursor(Qt.PointingHandCursor)
        self.judge_button_left.setStyleSheet(style.button_white)
        self.judge_button_left.setVisible(False)  # 默认隐藏

        judge_button_container_left = AlignedContainer(self.judge_button_left, QHBoxLayout, Qt.AlignmentFlag.AlignLeft)
        self.judgment_layout.addWidget(judge_button_container_left, 0, 0)

        ### 右侧按钮（提交/继续）
        self.judge_button_right = QPushButton("检查")
        self.judge_button_right.setFixedSize(150, 48)
        self.judge_button_right.setCursor(Qt.PointingHandCursor)
        self.judge_button_right.setStyleSheet(style.button_green)
        self.judge_button_right.setEnabled(False)

        ### 提交逻辑
        self.next_action: Literal["check", "next", "finish"] = "check"
        self.judge_button_right.clicked.connect(self.next)

        judge_button_container_right = AlignedContainer(
            self.judge_button_right, QHBoxLayout, Qt.AlignmentFlag.AlignRight
        )
        self.judgment_layout.addWidget(judge_button_container_right, 0, 4)

        # 音效
        self.se_correct = QSoundEffect(source=QUrl.fromLocalFile("resources/SE/correct.wav"))
        self.se_incorrect = QSoundEffect(source=QUrl.fromLocalFile("resources/SE/incorrect.wav"))
        self.se_finished = QSoundEffect(source=QUrl.fromLocalFile("resources/SE/finished.wav"))

    def clear_challenge(self):
        """清空当前题目"""
        layout = self.challenge_layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

    def update_challenge(self):
        self.clear_challenge()
        data = self.challenges[self.challenge_index]

        # 问题
        self.challenge_question = QLabel(data.question)
        self.challenge_question.setStyleSheet(
            "color: #3C3C3C; font-weight: bold; font-size: 32px; line-height: 1.25; margin: 0; text-align: left; width: 100%;"
        )
        self.challenge_question.setFixedHeight(40)

        # 选项
        self.challenge = data.create_challenge()

        def setCheckButtonEnable(flag):
            self.judge_button_right.setEnabled(flag)

        self.challenge.optionSelected.connect(setCheckButtonEnable)

        self.challenge_layout.addWidget(self.challenge_question)
        self.challenge_layout.addWidget(self.challenge)

    def next(self):
        """下一步操作（检查答案/下一题）"""
        match self.next_action:
            case "check":
                is_correct, answer = self.challenge.check_answer()

                # 播放音效
                if is_correct:
                    self.se_correct.play()
                else:
                    self.se_incorrect.play()

                # 显示信息面板
                self.judgment_container.setStyleSheet(f"background-color: {'#D7FFB8' if is_correct else '#FFDFE0'};")
                self.answer_result = (
                    AnswerResult(True, "正确！") if is_correct else AnswerResult(False, "正确答案：", answer)
                )
                self.judge_button_left.setVisible(False)
                self.judgment_layout.addWidget(self.answer_result, 0, 0, 1, 4)

                # 更新界面
                self.progress_bar.setValue(self.challenge_index + 1)
                self.judge_button_right.setStyleSheet(style.button_green if is_correct else style.button_red)

                self.next_action = "next"
            case "next":  # 下一题
                # 还原界面
                self.judge_button_right.setStyleSheet(style.button_green)
                self.judgment_container.setStyleSheet("border-top: 2px solid #E5E5E5")
                self.answer_result.setParent(None)
                self.answer_result.deleteLater()
                self.judgment_layout.addWidget(self.judge_button_left, 0, 0)

                # 切换题目
                self.challenge_index += 1
                if self.challenge_index >= len(self.challenges):
                    self.clear_challenge()
                    self.se_finished.play()
                    self.next_action = "finish"
                    return  # TODO: 结束单元
                self.update_challenge()
                self.judge_button_right.setEnabled(False)

                self.next_action = "check"
            case "finish":
                # TODO: 结算页面
                ...
            case other:
                raise ValueError(f"Unknown action {other}")


if __name__ == "__main__":
    application = QApplication()
    application.styleHints().setColorScheme(Qt.ColorScheme.Light)
    # 字体
    families = QFontDatabase.applicationFontFamilies(
        QFontDatabase.addApplicationFont(
            r"d:\MyPC\Advanced\Code\Python\Projects\openlingo\resources\fonts\DINRound.otf"
        )
    )
    duo_font = f"{families[0]}, " if families else ""
    font = QFont(f"{duo_font}Microsoft YaHei UI, sans-serif")
    application.setFont(font)

    window = QMainWindow()
    window.setWindowTitle("[DEBUG] Openlingo ChallengeUI")
    window.resize(900, 690)

    palette = window.palette()
    palette.setColor(window.backgroundRole(), QColor("#FFFFFF"))
    window.setPalette(palette)

    challenges = ChallengeData.from_json("test_challenges.json")
    app = ChallengeUI(challenges)
    # app.setStyleSheet("border: 1px solid black; outline: none;")
    app.setStyleSheet("outline: none;")
    app.challenge_question.setFont(font)
    window.setCentralWidget(app)

    window.show()

    application.exec()
