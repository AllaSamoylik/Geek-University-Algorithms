import sys
from memory_profiler import profile
from random import randint

numbers_range = [6, 2, 5, -1, -8, 4, 6, -8, 7, 9]
# numbers_range = [randint(-10, 10) for i in range(15)]
how_many = 2
numb_sum = 0

if 0 < how_many <= len(numbers_range):
    for n in range(0, how_many):
        numb_sum += numbers_range[n]
    print(numb_sum)
else:
    print('Некорректное количество элементов')

print(f'Переменная <numbers_range> занимает {sys.getsizeof(numbers_range)} байт')
print(f'Ссылок на объект: {sys.getrefcount(numbers_range)}')
print(f'Переменная <how_many> занимает {sys.getsizeof(how_many)} байт')
print(f'Ссылок на объект: {sys.getrefcount(how_many)}')
print(f'Переменная <numb_sum> занимает {sys.getsizeof(numb_sum)} байт')
print(f'Ссылок на объект: {sys.getrefcount(numb_sum)}\n')


# Переменные <how_many> и <numb_sum> ссылаются на целые числа int и занимают фиксированные 28 байт памяти.
# Переменная <numbers_range> ссылается на список, размер занимаемой памяти которого напрямую зависит
# от количества элементов (8 байт для каждого указателя на int) + доп.расходы на создание списка,
# хранение ссылок и пр.(56 байт).
#
# Причём расходы на "поддержание" постоянны только для заданного списка,
# в случае c List Comp. расходы будут заметно расти с ростом количества элементов.
# Если для 15 элементов разница на накладные расходы составляет 8 байт,
# то для 150 элементов - разница уже в 4 раза (56 байт и 240 байт).
#
# Для <numbers_range> была создана одна ссылка (+1 временная ссылка).
# Для <how_many> и <numb_sum> отображается большое количество ссылок в связи с тем,
# что они ссылаются на небольшие целые числа, которые используются многими внутренними переменными Python.


@profile
def my_matrix(n, m):
    matrix = [[randint(0, 100) for _ in range(m)] for _ in range(n)]
    # print(matrix, '\n')
    min_lst = []

    for col in range(m):
        min_el = matrix[0][col]
        for el in range(n):
            if matrix[el][col] < min_el:
                min_el = matrix[el][col]
        min_lst.append(min_el)
    return f'Среди min элементов столбцов {min_lst} max элемент - {max(min_lst)}'


print(my_matrix(3, 5))
#print(my_matrix(300, 300))

# Построчный анализ не выявил участков потребления кодом больших объемов памяти -
# оптимизация не требуется.
#
# Выделяемой памяти в 18.9 мебибайт хватает для небольших матриц до 50 х 50,
# точек прироста памяти нет. При масштабировании - начинает дополнительно
# использоваться память для поддержания вложенного List Comp.


# Windows_7 64x
# Python 3.8.10
