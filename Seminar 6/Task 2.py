#2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

numberN = 424

list = [i for i in range(20, numberN)
                if i % 20 == 0 or i % 21 == 0] 
print("Список чисел кратных 20 или 21 в диапазоне [20..N): ", list)