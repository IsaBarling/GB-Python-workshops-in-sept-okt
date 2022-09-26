# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.


day = int(input('Enter day number: '))
if day > 7 or day < 1:
     print('It is not the day of the week!')
elif day == 6 or day == 7:
     print("Yes, it's weekend!")
else:
    print("No, it's a working day!")