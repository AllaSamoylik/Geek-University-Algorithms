from random import randint

num_array = [randint(1, 100) for _ in range(10)]
print(num_array, '\n')
middle_sum = 0
idx_max = num_array.index(max(num_array))
idx_min = num_array.index(min(num_array))

if idx_min == idx_max + 1 or idx_max == idx_min + 1:
    print(f'Между min ({min(num_array)}) и max ({max(num_array)}) элементами нет элементов ')
else:
    for n in range(len(num_array)):
        if n == idx_min:
            while n < idx_max - 1:
                middle_sum += num_array[n+1]
                n += 1
        elif n == idx_max:
            while n < idx_min - 1:
                middle_sum += num_array[n+1]
                n += 1
    print(f'Сумма элементов между min ({min(num_array)}) и max ({max(num_array)}) элементами равна {middle_sum}')
