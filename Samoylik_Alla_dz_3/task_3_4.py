from random import randint, seed
seed(1)

array = [randint(1, 100) for _ in range(1000)]

unique_array = list(set(array))
counters = [0 for _ in range(len(unique_array))]

for i in unique_array:
    for j in array:
        if i == j:
            counters[unique_array.index(i)] += 1

most_number = max(counters)

if most_number != 1:
    for idx in range(len(counters)):
        if counters[idx] == most_number:
            print(f'Чаще всего ({counters[idx]} раз) встречается число {unique_array[idx]}')
else:
    print(f'Все числа в массиве встречаются не больше одного раза')
