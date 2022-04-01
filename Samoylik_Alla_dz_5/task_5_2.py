from collections import deque

hex_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
inv_hex_int = {value: key for key, value in hex_int.items()}


def hex_add(numb1, numb2):
    hex_numb1 = numb1[:]
    hex_numb2 = numb2[:]
    memorize = 0
    answer = []

    if len(hex_numb2) > len(hex_numb1):
        hex_numb2, hex_numb1 = hex_numb1, hex_numb2

    # Сложение
    while len(hex_numb2) > 0:
        sum = hex_int[hex_numb1[-1]] + hex_int[hex_numb2[-1]] + memorize
        if sum >= 16:
            answer.append(inv_hex_int[sum - 16])
            memorize = 1
        else:
            answer.append(inv_hex_int[sum])
            memorize = 0
        hex_numb1.pop()
        hex_numb2.pop()

    # Добавляем оставшиеся
    if hex_numb1:
        for symbols in hex_numb1[::-1]:
            answer.append(symbols)
    answer.reverse()

    return answer


def hex_mult(numb1, numb2):
    hex_numb1 = numb1[:]
    hex_numb2 = numb2[:]
    memorize = 0
    answer = []

    if len(hex_numb2) > len(hex_numb1):
        hex_numb2, hex_numb1 = hex_numb1, hex_numb2

    # Умножаем
    for symbol2 in hex_numb2[::-1]:
        mult_list = []
        for symbol1 in hex_numb1[::-1]:
            mult = hex_int[symbol2] * hex_int[symbol1] + memorize
            if mult >= 16:
                mult_list.append(mult % 16)
                memorize = mult // 16
            else:
                mult_list.append(mult)
                memorize = 0
        if memorize != 0:
            mult_list.append(memorize)
            memorize = 0
        answer.append(mult_list)

    # Приводим к очередям
    for i in range(len(answer)):
        dq_answer = deque(answer[i])
        answer[i] = dq_answer

    # Добавляем нули в начало
    zeros_number = 1
    for i in answer[1:]:
        i.extendleft([0] * zeros_number)
        zeros_number += 1

    # Добавляем нули в конец
    zeros_number = len(answer) - 1
    for i in answer[:len(answer) - 1]:
        i.extend([0] * zeros_number)
        zeros_number -= 1

    # Суммируем элементы в каждом подсписке
    zip_answer = list(zip(*answer))
    map_answer = list(map(sum, zip_answer))

    mem = 0
    for el in range(len(map_answer) - 1):
        if map_answer[el] + mem >= 16:
            map_answer[el] %= 16
            mem = map_answer[el] // 16
        else:
            mem = 0
    map_answer.reverse()

    return list(inv_hex_int[el] for el in map_answer)


hex_numb1 = list(input('Первое шестнадцатиричное число: '))
hex_numb2 = list(input('Второе шестнадцатиричное число: '))

print(hex_add(hex_numb1, hex_numb2))
print(hex_mult(hex_numb1, hex_numb2))

# Ну или :)

# hex_numb1 = list(input('Первое шестнадцатиричное число: '))
# hex_numb2 = list(input('Второе шестнадцатиричное число: '))
#
# sum = hex(int(''.join(hex_numb1), 16) + int(''.join(hex_numb2), 16)).lstrip('0x').upper()
# mult = hex(int(''.join(hex_numb1), 16) * int(''.join(hex_numb2), 16)).lstrip('0x').upper()
#
# print(f'Сумма чисел {hex_numb1} и {hex_numb2} равна {[digit for digit in sum]}')
# print(f'Произведение чисел {hex_numb1} и {hex_numb2} равно {[digit for digit in mult]}')
