from random import randint

n, m = 5, 3
# создание матрицы:
# matrix = [[0]*m for i in range(n)]
# заполнение руками:
# matrix = [[int(input('Введите элемент: ')) for el in range(m)] for l in range(n)]
matrix = [[randint(0, 10) for y in range(m)] for x in range(n)]
print(matrix, '\n')

for line in range(n):
    sum = 0
    for el in range(m):
        sum += matrix[line][el]
    matrix[line].append(sum)
    # или
    # matrix[line][m:] = [sum]

for l in matrix:
    row = '\t'.join(map(str, l))
    print(row)
