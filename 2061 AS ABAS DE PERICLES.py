n, m = input().split(' ')
n = int(n)
m = int(m)
mais = menos = 0

for c in range(0, m):
    resp = input().lower()
    if resp == 'fechou':
        n += 1
    elif resp == 'clicou':
        n -= 1

print(n)
