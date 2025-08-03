import random
from enum import Enum


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
