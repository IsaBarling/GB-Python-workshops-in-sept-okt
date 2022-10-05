# 1. Вычислить число c заданной точностью d

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number

num1 = InputNumbers("Введите 1 число: ")
n = int(InputNumbers("Введите точность (количество знаков после запятой): "))
rezult = round((num1), n)

print(f"Число с заданной точностью: {rezult}")