# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите количество чисел в списке '))

def numbers(n):
    summ = 0
    for i in range(n):
        a = int(input(f'Введи число {i + 1} '))
        a = (1+1/a)**a
        summ = a + summ
        i += 1
    return summ

print('Сумма чисел равна',round((numbers(n)), 2))