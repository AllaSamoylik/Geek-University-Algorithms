from random import randint

numbers = [randint(-50, 50) for _ in range(10)]
print(numbers, '\n')

neg_nambers = [n for n in numbers if n < 0]
max_number = max(neg_nambers)

print(f'Максимальный отрицательный элемент: {max_number}  на позиции {numbers.index(max_number)+1}')
