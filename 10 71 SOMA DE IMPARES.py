soma = 0
x = int(input())
y = int(input())

if x <= y:
    for c in range(x+1, y):
        if c % 2 != 0:
            soma += c
else:
    for c in range(y+1, x):
        if c % 2 != 0:
            soma += c

print(soma)
