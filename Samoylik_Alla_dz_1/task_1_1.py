
numb = int(input('Введите трёхзначное число: '))

first = numb // 100
second = numb % 100 // 10
last = numb % 10

summ = first + second + last
mult = first * second * last

print(f'Сумма цифр - {summ}')
print(f'Произведение цифр - {mult}')
