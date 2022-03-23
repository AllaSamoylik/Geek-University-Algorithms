from random import randint

num_array = [randint(1, 100) for _ in range(10)]
print(num_array, '\n')

idx_max = 0
idx_min = 0

for i in range(1, len(num_array)):
    if num_array[i] > num_array[idx_max]:
        idx_max = i
    elif num_array[i] < num_array[idx_min]:
        idx_min = i
num_array[idx_max], num_array[idx_min] = num_array[idx_min], num_array[idx_max]

print(f'Максимальный элемент - {num_array[idx_max]}')
print(f'Минимальный элемент - {num_array[idx_min]}')
print(num_array)
