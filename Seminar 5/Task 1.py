# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

myStory = input("Введите текст через пробел:\n")

def DeleteABCtext(myStory):
    myStory = list(filter(lambda x: 'абв' not in x, myStory.split()))
    return " ".join(myStory)


myStory = DeleteABCtext(myStory)
if len(myStory) == 0:
    print("Кажется, эта строка осталась пустой: ")
print(myStory)
