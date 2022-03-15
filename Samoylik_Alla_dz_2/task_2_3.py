number = input('Введите натуральное число: ')
numb_list = list(map(str, str(number)))

print(''.join(numb_list[::-1]))

# Или

number = int(input('Введите натуральное число: '))
numb_list = []

while number:
    numb_list.append(number % 10)
    number //= 10
numb_mod = [str(n) for n in numb_list]

print(''.join(numb_mod))
