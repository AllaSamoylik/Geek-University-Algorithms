
letter_1, letter_2 = input('Введите две строчные буквы английского алфавита: \n').split()

if letter_1 != letter_2:
    if ord('a') <= ord(letter_1) <= ord('z') and ord('a') <= ord(letter_2) <= ord('z'):
        place_1 = ord(letter_1) - ord('a') + 1
        place_2 = ord(letter_2) - ord('a') + 1
        print(f'Буква "{letter_1}" стоит на {place_1} месте в алфавите, буква "{letter_2}" - на {place_2} месте')
        if place_1 < place_2:
            place_dif = place_2 - place_1 - 1
            print(f'Между ними {place_dif} букв(ы)')
        else:
            place_dif = place_1 - place_2 - 1
            print(f'Между ними {place_dif} букв(ы)')
    else:
        print('Вычисление невозможно: один / оба символа не являются строчными буквами английского алфавита')
else:
    print('Вычисление невозможно: введены две одинаковые буквы')


'''
Первый вариант:

a, b = input('Введите две строчные буквы английского алфавита: \n').split()

letters_list = [None]
for i in range(ord('a'), ord('z')+1):
    letters_list.append(i)

if a != b:
    if ord(a) in letters_list:
        a_place = letters_list.index(ord(a))
        if ord(b) in letters_list:
            b_place = letters_list.index(ord(b))
            print(f'Буква "{a}" стоит на {a_place} месте в алфавите, буква "{b}" - на {b_place} месте')
            if a_place < b_place:
                print(f'Между ними {b_place - a_place} букв(ы)')
            else:
                print(f'Между ними {a_place - b_place} букв(ы)')
        else:
            print('Указанной (второй) буквы в алфавите нет')
    else:
        print('Указанной (первой) буквы в алфавите нет')
else:
    print('Введены две одинаковые буквы')
'''
