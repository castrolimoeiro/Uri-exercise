n = int(input())

for i in range(0, n):
    soma = 0
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    if x < y:
        for c in range(x+1, y):
            if c % 2 != 0:
                soma += c
        print(soma)
    elif x > y:
        for c in range(y+1, x):
            if c % 2 != 0:
                soma += c
        print(soma)
    elif x == y:
        print(soma)
