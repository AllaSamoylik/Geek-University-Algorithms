
letter_place = int(input('Введите номер места строчной буквы в английском алфавите: \n'))

code = ord('a') + letter_place - 1

if ord('a') <= code <= ord('z'):
    letter = chr(code)
    print(letter)
else:
    print('Вычисление невозможно: введенный номер не соответствует ни одной строчной букве английского алфавита')
