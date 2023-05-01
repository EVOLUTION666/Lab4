import re

txt = ""
with open("text.txt", "r", encoding='utf-8') as f:
    # noinspection PyRedeclaration
    txt = f.readlines()
    print(txt)


if not txt:
    print("File is empty")
    exit()

assert txt != ""