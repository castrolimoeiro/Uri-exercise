while True:
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    soma = 0
    if x <= 0 or y <= 0:

        break
    elif x < y:
        for c in range(x, y + 1):
            print(f'{c}', end=' ')
            soma += c
        print(f'Sum={soma}')

    elif y < x:
        for c in range(y, x + 1):
            print(f'{c}', end=' ')
            soma += c
        print(f'Sum={soma}')
