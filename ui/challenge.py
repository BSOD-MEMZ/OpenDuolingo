from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QFontDatabase, QPixmap
from PySide6.QtWidgets import (
    QApplication,
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


class AlignedContainer(QWidget):
    """自动对齐的容器"""

    def __init__(
        self,
        parent: QWidget | None = None,
        widget: QWidget | None = None,
        layout: type[QLayout] = QHBoxLayout,
        align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        no_margin: bool = True,
    ):
        super().__init__(parent)
        _layout = layout(self)
        _layout.setAlignment(align)
        if no_margin:
            _layout.setContentsMargins(0, 0, 0, 0)

        _layout.addWidget(widget if widget else QWidget())


class ChallengeUI(QWidget):
    """通用答题界面"""

    def __init__(self, parent: QWidget | None = None, challenge: QWidget | None = None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Status Area
        self.status_area = QWidget()
        self.status_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.status_area.setMaximumWidth(1080)
        self.status_area.setFixedHeight(32)

        status_container = AlignedContainer(
            self, self.status_area, QHBoxLayout, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter
        )
        status_container.setContentsMargins(40, 0, 40, 18)
        status_container.setFixedHeight(100)
        layout.addWidget(status_container)

        # Challenge Area

        self.challenge_area = QWidget()
        self.challenge_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.challenge_area.setMaximumSize(600, 450)
        self.challenge_area.setMinimumHeight(400)

        challenge_container = AlignedContainer(self, self.challenge_area, QHBoxLayout, Qt.AlignmentFlag.AlignHCenter)
        challenge_container.setMinimumWidth(700)

        layout.addWidget(challenge_container)

        # Judgment Area

        self.judgment_area = QFrame()
        self.judgment_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.judgment_area.setMaximumWidth(1000)

        judgment_container = AlignedContainer(self, self.judgment_area, QHBoxLayout, Qt.AlignmentFlag.AlignHCenter)
        judgment_container.setFixedHeight(140)

        layout.addWidget(judgment_container)

        ## 内部
        # Status Area
        status_layout = QGridLayout(self.status_area)
        status_layout.setContentsMargins(0, 0, 0, 0)
        status_layout.setHorizontalSpacing(24)

        # 退出按钮
        self.exit_button = QPushButton()
        self.exit_button.setIcon(QPixmap("resources/icons/exit.png"))
        self.exit_button.setFixedSize(32, 32)
        self.exit_button.setStyleSheet("background: none; border: none; qproperty-iconSize: 20px 20px;")
        self.exit_button.setCursor(Qt.PointingHandCursor)

        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.progress_bar.setFixedHeight(16)

        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet(style.progress_bar)
        self.progress_bar.setRange(0, 15)
        self.progress_bar.setValue(6)

        # 红心数
        self.heart_count_display = QWidget()
        self.heart_count_display.setFixedWidth(50)

        status_layout.addWidget(self.exit_button, 0, 0)
        status_layout.addWidget(self.progress_bar, 0, 1)
        status_layout.addWidget(self.heart_count_display, 0, 2)

        # Challenge Area
        challenge_layout = QVBoxLayout(self.challenge_area)
        challenge_layout.setContentsMargins(0, 0, 0, 0)
        challenge_layout.setSpacing(24)

        self.challenge_header = QLabel('选择 "homo1145" 对应的字符')
        self.challenge_header.setStyleSheet(
            "color: #3C3C3C; font-weight: bold; font-size: 32px; line-height: 1.25; margin: 0; text-align: left; width: 100%;"
        )
        self.challenge_header.setFixedHeight(40)
        challenge_layout.addWidget(self.challenge_header)

        # 题目组件
        if challenge:
            self.challenge = challenge
        else:
            self.challenge = QLabel("Place Holder")
            self.challenge.setStyleSheet("border: 1px solid black; font-size: 48px")
        challenge_layout.addWidget(self.challenge)

        # Judgment Area
        self.judgment_area.setStyleSheet("QFrame { padding: 0px 40px; }")
        judgment_layout = QGridLayout(self.judgment_area)
        judgment_layout.setContentsMargins(0, 0, 0, 0)
        judgment_layout.setHorizontalSpacing(16)

        for i in range(5):
            judgment_layout.setColumnStretch(i, 1)

        # 左侧按钮
        self.judge_button_left = QPushButton("跳过")
        self.judge_button_left.setFixedSize(150, 48)
        self.judge_button_left.setCursor(Qt.PointingHandCursor)
        self.judge_button_left.setStyleSheet(style.button_white)

        judge_button_container_left = AlignedContainer(
            self.judgment_area, self.judge_button_left, QHBoxLayout, Qt.AlignmentFlag.AlignLeft
        )
        judgment_layout.addWidget(judge_button_container_left, 0, 0)

        # 右侧按钮
        self.judge_button_right = QPushButton("检查")
        self.judge_button_right.setFixedSize(150, 48)
        self.judge_button_right.setCursor(Qt.PointingHandCursor)
        self.judge_button_right.setStyleSheet(style.button_green)

        judge_button_container_right = AlignedContainer(
            self.judgment_area, self.judge_button_right, QHBoxLayout, Qt.AlignmentFlag.AlignRight
        )
        judgment_layout.addWidget(judge_button_container_right, 0, 4)


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

    app = ChallengeUI(window)
    app.setStyleSheet("outline: none;")
    app.challenge_header.setFont(font)
    window.setCentralWidget(app)

    window.show()

    application.exec()
