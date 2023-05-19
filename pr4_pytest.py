from regexp import regex_matcher

def test1_regex_matcher():
    with open("text_ep.txt", mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        new_text = regex_matcher(lines)
    assert new_text == 'ИванИванов|27|+79990001111|Invalid mail\nИванИванов|27|+79990001111|example@yandex.ru\n'
