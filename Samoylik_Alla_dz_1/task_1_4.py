
import random

first_element, last_element = input('Задайте границы диапозона: \n').split()
gen = ''

if first_element.isdigit() and last_element.isdigit():
    gen = random.randint(int(first_element), int(last_element))
elif first_element.replace('.', '', 1).isdigit() and last_element.replace('.', '', 1).isdigit():
    gen = random.uniform(float(first_element), float(last_element))
elif first_element.isalpha() and last_element.isalpha():
    gen = chr(random.randint(ord(first_element), ord(last_element)))
else:
    print('Генерация невозможна: задан некорректный символ/число')

print(f'Случайный элемент - {gen}')
