num_array = [8, 3, 15, 6, 4, 2]

even_array = [num_array.index(n) for n in num_array if n % 2 == 0]
print(even_array)
