n = int(input('Введите количество элементов: '))
numbers_range = [1, -0.5, 0.25, -0.125]
numb_sum = 0

if 0 < n <= len(numbers_range):
    for n in range(0, n):
        numb_sum += numbers_range[n]
    print(numb_sum)
else:
    print('Некорректное количество элементов')
