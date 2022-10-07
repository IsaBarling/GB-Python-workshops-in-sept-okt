#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from mailbox import linesep
from xml.dom.minidom import Document


with open("text_words.txt", "r") as data:
    lines = data.readlines()
    print(lines)
