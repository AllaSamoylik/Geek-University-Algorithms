
n1 = 5
n2 = 6

n1_binary = bin(n1)
n2_binary = bin(n2)

bitwise_and = n1 & n2
bitwise_or = n1 | n2
bitwise_xor = n1 ^ n2
bitwise_ls = n1 << 2
bitwise_rs = n1 >> 2

print(f'{n1} в двоичной системе счисления - {n1_binary},\n\
{n2} в двоичной системе счисления - {n2_binary}\n')

print(f'Побитовый оператор AND: {bitwise_and}')
print(f'Побитовый оператор OR: {bitwise_or}')
print(f'Побитовый оператор XOR: {bitwise_xor}')
print(f'Побитовый сдвиг влево: {bitwise_ls}')
print(f'Побитовый сдвиг вправо: {bitwise_rs}')
