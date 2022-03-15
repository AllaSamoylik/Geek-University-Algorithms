number = input('Введите натуральное число: ')
even = []
odd = []

for n in number:
    if int(n) % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(f'В числе {number}: {len(even)} чётных и {len(odd)} нечётных цифр')

# Или

def even_odd(numb):
    global even
    global odd
    while numb > 0:
        if numb % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd(numb // 10)
    print(f'Чётных - {even}, нечётных - {odd}')


even = 0
odd = 0

even_odd(int(input('Введите натуральное число: ')))
