while True:
    sign = input('Введите знак (или "0" для выхода): ')
    if sign != '0':
        if sign in ('+', '-', '*', '/'):
            a = int(input('Первое число: '))
            b = int(input('Второе число: '))
            if sign == '+':
                print(f'{a} {sign} {b} = {a + b}')
            elif sign == '-':
                print(f'{a} {sign} {b} = {a - b}')
            elif sign == '*':
                print(f'{a} {sign} {b} = {a * b}')
            elif sign == '/':
                while b != 0:
                    print(f'{a} {sign} {b} = {a / b}')
                    break
                else:
                    print('Ошибка деления на ноль')
        else:
            print('Введён неверный знак')
    else:
        break
