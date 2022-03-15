import random

secret = random.randint(0, 100)
attempt = 1

while attempt <= 10:
    guess = int(input(f'Ваша {attempt} попытка: '))
    if guess > secret:
        print(f'Загаданное число меньше')
        attempt += 1
    elif guess < secret:
        print(f'Загаданное число больше')
        attempt += 1
    else:
        print(f'Угадали, это число - {guess}')
        break
else:
    print(f'Попыток больше нет. Было загадано число - {secret} ')
