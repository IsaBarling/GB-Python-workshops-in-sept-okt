#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

from email.generator import DecodedGenerator
import os 

def rleAlgorithmEncode(line):
    #return'abc'
    encLine = ''
    count = 1
    char = line[0]
    for i in range(1, len(line)):
        if line[i] == char:
            count += 1
        else:
            encLine += str(count) + char
            count = 1
            char = line[i]
    encLine += str(count) + char
    return encLine

def rleAlgorithmDecode(line):
    decLine = ''
    charAmount = ''
    nums = ['0','1','2','3','4','5','6','7','8','9']
    char = ''
    for i in range(len(line)):
        if line[i] in nums:
            charAmount += line[i]
        else:
            if len(charAmount) != 0:
                decLine += int(charAmount)*line[i]
                charAmount = ''
    return decLine



encodedLines = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'text_words.txt'), 'r') as data:
    lines = data.readlines()
    print(lines)
    for i in range(0, len(lines)):
        encodedLines.append(rleAlgorithmEncode(lines[i])) 
        
with open(os.path.join(__location__, 'text_code_words.txt'), 'w') as dataTwo:
    for line in encodedLines:
        dataTwo.write(line + '\n')
    print(encodedLines)

with open(os.path.join(__location__, 'text_code_words.txt'), 'r') as dataThree:
    lines = dataThree.readlines()
    decodedLines = ''
    print(len(lines))
    for i in range(0, len(lines)):
        decodedLines += rleAlgorithmDecode(lines[i])
    print(decodedLines)





    