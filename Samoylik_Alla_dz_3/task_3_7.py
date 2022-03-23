from random import randint

num_array = [randint(1, 100) for _ in range(10)]
print(num_array)
min_list = []
m = None

while len(min_list) != 2:
    min = num_array[0]
    for m in num_array:
        if m < min:
            min = m
    min_list.append(min)
    num_array.pop(num_array.index(min))

print(f'Два наименьших элемента в масссиве: {" и ".join(str(i) for i in min_list)}' '\n')

# или

num_array = [randint(1, 100) for _ in range(10)]
print(num_array)
min_list = sorted(num_array)[:2:]

print(f'Два наименьших элемента в масссиве: {" и ".join(str(i) for i in min_list)}')