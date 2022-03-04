
a, b, c = map(int, input('Введите три разных числа: \n').split())

if b < a < c or c < a < b:
    print(f'Средним является число {a}')
elif a < b < c or c < b < a:
    print(f'Средним является число {b}')
else:
    print(f'Средним является число {c}')

'''
Или:
numbers_list = list(map(int, input('Введите длину трёх отрезков: \n').split()))

mean = sorted(numbers_list)[1]

print(f'Средним является число {mean}')
'''