# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indices_in_range(lst, min_value, max_value):
    indices = []
    for i, value in enumerate(lst):
        if min_value <= value <= max_value:
            indices.append(i)
    return indices

min_value = int(input('Введите минимум диапазона, от 1 до 100:'))
max_value = int(input('Введите максимум диапазона, от 1 до 100:'))
list1 = [i for i in range(1,100) if i % 5 == 0]

result = find_indices_in_range(list1, min_value, max_value)

print(f"Индексы элементов в диапазоне от {min_value} до {max_value}: {result}")
