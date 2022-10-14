#2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


def new_list():
    return [i for i in range(20, 424)
                if i % 20 == 0 or i % 21 == 0] 
new_list()
print("Список чисел кратных 20 или 21 в диапазоне [20..N): ")
print(new_list())