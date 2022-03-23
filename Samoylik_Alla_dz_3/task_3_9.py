from random import randint

n, m = 5, 3
matrix = [[randint(0, 100) for y in range(m)] for x in range(n)]
print(matrix, '\n')
min_lst = []

for col in range(m):
    min_el = matrix[0][col]
    for el in range(n):
        if matrix[el][col] < min_el:
            min_el = matrix[el][col]
    min_lst.append(min_el)

print(f'Среди min элементов столбцов {min_lst} max элемент - {max(min_lst)}')
