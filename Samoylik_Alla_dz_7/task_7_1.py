from random import randint


def comb_sort(data):
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True
    return data


n = 10
array = [randint(-100, 99) for i in range(n)]

print('Исходный массив:', '\n', array, '\n')
print('Отсортированный массив:', '\n', comb_sort(array))
