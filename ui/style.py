button_option = """
QPushButton {
    color: #4B4B4B;
    background-color: #FFFFFF;
    border: 2px solid #E5E5E5;
    border-radius: 12px;
    border-width: 2px 2px 4px;
    padding: 0 16px;
    /* font-size: 72px; */
    letter-spacing: 0.8px;
    text-decoration: none;
}
QPushButton:hover {
    background-color: #F7F7F7;
}
QPushButton:pressed {
    margin-top: 2px;
    border-bottom-width: 2px;
}
QPushButton:checked {
    color: #1899D6;
    background-color: #DDF4FF;
    border-color: #84D8FF;
}
QPushButton[correct="true"] {
    color: #58A700;
    background-color: #D7FFB8;
    border-color: #A5ED6E;
}
"""

button_green = """
QPushButton {
    color: #FFFFFF;
    background-color: #58CC02;
    border: 2px solid #58A700;
    border-radius: 16px;
    border-width: 0px 0px 4px;
    padding: 0 16px;
    font-size: 17px;
    font-weight: bold;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    text-decoration: none;
}
QPushButton:hover {
    background-color: #61E002;
    border-color: #61B800;
}
QPushButton:pressed {
    margin-top: 2px;
    border-bottom-width: 2px;
}
QPushButton:disabled {
    color: #AFAFAF;
    background-color: #E5E5E5;
    border-color: #E5E5E5;
    margin-top: 2px;
    border-bottom-width: 2px;
}
"""


button_red = """
QPushButton {
    color: #FFFFFF;
    background-color: #FF4B4B;
    border: 2px solid #EA2B2B;
    border-radius: 16px;
    border-width: 0px 0px 4px;
    padding: 0 16px;
    font-size: 17px;
    font-weight: bold;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    text-decoration: none;
}
QPushButton:hover {
    background-color: #FF5252;
    border-color: #FF2F2F;
}
QPushButton:pressed {
    margin-top: 2px;
    border-bottom-width: 2px;
}
QPushButton:disabled {
    color: #AFAFAF;
    background-color: #E5E5E5;
    border-color: #E5E5E5;
    margin-top: 2px;
    border-bottom-width: 2px;
}
"""

button_white = """
QPushButton {
    color: #AFAFAF;
    background-color: #FFFFFF;
    border: 2px solid #E5E5E5;
    border-radius: 16px;
    border-width: 2px 2px 4px;
    padding: 0 16px;
    font-size: 17px;
    font-weight: bold;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    text-decoration: none;
}
QPushButton:hover {
    color: #9D9D9D;
    background-color: #E5E5E5;
    border-color: #CECECE;
}
QPushButton:pressed {
    margin-top: 2px;
    border-bottom-width: 2px;
}
QPushButton:disabled {
    color: #AFAFAF;
    background-color: #E5E5E5
    margin-top: 2px;
    border-bottom-width: 2px;
}
"""

progress_bar = """
QProgressBar {
    border-radius: 7px;
    background-color: #E5E5E5;
}

QProgressBar::chunk {
    border-radius: 7px;
    background-color: #58CC02;
}
"""
