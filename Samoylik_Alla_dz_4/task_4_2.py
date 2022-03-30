import cProfile


# Решето
def erat_1(n):
    # n = int(input('Введите позицию простого числа (1>>>): '))
    max_num = 0

    numb_dict = {10: 29,
                 10 ** 2: 541,
                 10 ** 3: 7919
                 }

    for key in numb_dict.keys():
        if n <= key:
            max_num = numb_dict[key]
            break

    numbers = [i for i in range(max_num + 1)]
    numbers[1] = 0

    for i in range(2, max_num):
        if numbers[i] != 0:
            j = i + i
            while j <= max_num:
                numbers[j] = 0
                j += i
    erat_numbers = [i for i in numbers if numbers[i] != 0]

    return erat_numbers[n - 1]


# Не решето
def erat_2(n):
    # n = int(input('Введите позицию простого числа (1>>>): '))
    lst = []
    i = 2
    counter = 0

    while counter < n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
            counter += 1
        i += 1

    return lst[-1]


print(erat_1(6))
print(erat_2(6))
print('\n')

cProfile.run('erat_1(500)')
cProfile.run('erat_2(500)')

'''
По итогам оценки выяснилось, что хоть и у обоих алгоритмов квадратичное время из-за вложенных циклов, 
алгоритм с использованием "решета" во много раз эффективнее по времени, 
всего 7 вызовов и все функции вызывались по одному разу.

Алгоритм с сортировкой простых чисел посредством наличия делителей целесообразен 
к использованию только для небольших позиций искомого числа (до 50).
'''
