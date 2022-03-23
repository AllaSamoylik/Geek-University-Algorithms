num_first = 2
num_last = 9
num_range_st = 2
num_range_fin = 99

for num in range(num_first, num_last + 1):
    sum = 0
    for num_r in range(num_range_st, num_range_fin + 1):
        if num_r % num == 0:
            sum += 1
    print(f'Числу {num} кратно {sum} чисел')

print('*' * 20)

# или

counters = [0 for _ in range(2, 10)]

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            counters[j - 2] += 1

for n in range(2, 10):
    print(f'Числу {n} кратно {counters[n - 2]} чисел')
