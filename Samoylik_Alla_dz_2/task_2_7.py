n = int(input('Введите натуральное число (1>>>): '))
number = 1
numb_list = []

while number <= n:
    numb_list.append(number)
    number += 1
if sum(numb_list) == n * (n + 1) / 2:
    print('Равенство выполняется')

# Или

def numbers_sum(n):
    return n + numbers_sum(n - 1) if n != 1 else 1


n = int(input('Введите натуральное число (1>>>): '))

if numbers_sum(n) == n * (n + 1) / 2:
    print('Равенство выполняется')
