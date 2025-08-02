from typing import Literal

kana_list: list[dict[Literal["hiragana", "katakana", "romaji"], str]] = [
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

# 使用平假名索引
hira_to = {k["hiragana"]: k for k in kana_list}
# 使用片假名索引
kata_to = {k["katakana"]: k for k in kana_list}
# 使用罗马音索引
roma_to = {k["romaji"]: k for k in kana_list}
