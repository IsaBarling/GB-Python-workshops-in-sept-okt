#3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def ListOfColleagues(*names):
    output = {}
    for name in names:
        key = name[0].capitalize()
        if key not in output:
            output[key] = []
        output[key].append(name)
    return output

print(ListOfColleagues("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))