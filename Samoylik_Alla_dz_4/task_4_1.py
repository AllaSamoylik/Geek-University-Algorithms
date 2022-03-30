import cProfile
import timeit


def reverse_1(number):
    return str(number)[::-1]


def reverse_2(number):
    numb_list = []
    while number:
        numb_list.append(number % 10)
        number //= 10
    numb_mod = [str(n) for n in numb_list]

    return ''.join(numb_mod)


def reverse_3(number):
    numb = ''
    for n in str(number):
        numb = n + numb
    return numb


def reverse_4(number):
    if len(str(number)) == 1:
        return number
    else:
        return str(int(number) % 10) + reverse_4(str(int(number) // 10))


print(reverse_1(25896))
print(reverse_2(25896))
print(reverse_3(25896))
print(reverse_4(25896))
print('\n')

print(timeit.timeit(reverse_1(7 ** 1000)))
print(timeit.timeit(reverse_2(7 ** 1000)))
print(timeit.timeit(reverse_3(7 ** 1000)))
print(timeit.timeit(reverse_4(7 ** 1000)))
print('\n')

cProfile.run('reverse_1(9**1000)')
cProfile.run('reverse_2(9**1000)')
cProfile.run('reverse_3(9**1000)')
cProfile.run('reverse_4(9**1000)')

'''
Асимптотика всех алгоритмов O(n) - выполняются за линейное время.

Самый "питонистый" вариант со срезом является самым быстрым (очевидно при увеличении размера данных).
Второй по оптимальности - алгоритм с циклом for in, плюс его легко переложить на другие языки.

Самым неэффективным алгоритмом ожидаемо оказалась рекурсия - работает значительно медленнее,
большое количество вызовов, к тому же ограничена наполнением стека.
'''
