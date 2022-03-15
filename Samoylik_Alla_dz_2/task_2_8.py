def digit_look(number, digit):
    counter = 0
    for n in number:
        counter += 1 if n == digit else 0
    return counter


digit = input('Ищем цифру: ')
total = 0

for once in range(int(input('Введите количество чисел: '))):
    total += digit_look(input('Введите число: '), digit)

print(f'В введённых числах цифра {digit} встречается {total} раз(а)')
