def digits_sum(numb):
    return sum(map(int, str(numb)))


numb_list = list(map(int, input('Введите числа (через пробел): ').split()))
max_by_sum = 0
number = 0

for n in numb_list:
    sum_of_digits = digits_sum(n)
    if sum_of_digits > max_by_sum:
        max_by_sum = sum_of_digits
        number = n

print(f'Наибольшее по сумме цифр число - {number}, сумма его цифр - {max_by_sum}')
