#Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

from random import randint
from sympy import symbols
from math import prod
 
max_val=100
k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
koeff=[randint(-max_val ,max_val) for i in range(k)]+[randint(1,max_val)]
x = symbols('x')
print (sum(map(prod,zip(koeff,[x**i for i in range(k+1)]))), '= 0')