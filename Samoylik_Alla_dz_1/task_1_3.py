
x1, y1 = map(float, input('Введите координаты первой точки: ').split())
x2, y2 = map(float, input('Введите координаты второй точки: ').split())

if x1 == x2 and y1 == y2:
    print('Вычисление невозможно: координаты точек совпадают')
else:
    if x1 == x2:
        print(f'x = {x1:.2f}')
    elif y1 == y2:
        print(f'y = {y1:.2f}')
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y2 - k * x2
        if b >= 0:
            print(f'y = {k:.2f} x + {b:.2f}')
        else:
            print(f'y = {k:.2f} x - {abs(b):.2f}')
