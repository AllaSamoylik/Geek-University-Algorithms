first = 32
last = 127
step = 10
stop = first + step

for i in range(first, last + 1):
    if i < stop:
        print(f'{i}-{chr(i)} ', end="")
        i += 1
    else:
        print(f'\n{i}-{chr(i)} ', end="")
        stop += step

print('\n')

# Или

def code_char(f, l, stop):
    if f < l:
        if f < stop:
            return f'{str(f)}-{str(chr(f))} {str(code_char(f + 1, l, stop))}'
        else:
            return f'\n{str(f)}-{str(chr(f))} {(code_char(f + 1, l, stop + 10))}'
    else:
        return f'{str(f)}-{str(chr(f))}'


print(code_char(32, 127, 42))
