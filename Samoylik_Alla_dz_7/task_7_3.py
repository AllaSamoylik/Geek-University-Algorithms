from random import randint


# Поиск min и max элементов в массиве
def min_max(array):
    min = array[0]
    max = array[0]
    for el in array:
        if el > max:
            max = el
        if el < min:
            min = el
    return min, max


m = randint(1, 10)
array = [randint(1, 100) for i in range(2 * m + 1)]

left_part = []
right_part = []
part_size = len(array) // 2
median = 0

# Предполагаем медиану
is_median = (min_max(array)[0] + min_max(array)[1]) // 2
while is_median not in array:
    is_median += 1

# Относительно неё разбиваем массив на 2 части
for el in array:
    if el >= is_median:
        right_part.append(el)
    else:
        left_part.append(el)

# Перемещаем элементы до равновесия массивов
if len(left_part) > len(right_part):
    while len(right_part) != part_size + 1:
        median = min_max(left_part)[1]
        right_part.append(left_part.pop(left_part.index(median)))
    right_part.pop()
else:
    while len(left_part) != part_size + 1:
        median = min_max(right_part)[0]
        left_part.append(right_part.pop(right_part.index(median)))
    left_part.pop()

print('Исходный массив:', '\n', array)
print('*** Медиана для сверки:', sorted(array)[m], '\n')
print('Отсортированный массив:', '\n', left_part + [median] + right_part)
print('Медиана:', median)
