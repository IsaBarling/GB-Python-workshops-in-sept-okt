# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def intToBin(n):
    bits = []

    bits.append(str(0 if n%2 == 0 else 1))
    while n > 1:
        n = n // 2
        bits.append(str(0 if n%2 == 0 else 1))

    bits.reverse()
    return ''.join(bits)

n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))

print(intToBin(n))

