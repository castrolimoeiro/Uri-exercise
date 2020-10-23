n = int(input())
coelho = rato = sapo = contador = 0

for i in range(0, n):
    q, t = input().split(' ')
    t = t.upper()
    q = int(q)
    if 1 <= q <= 15:
        contador += q
        if t == 'C':
            coelho += q
        elif t == 'R':
            rato += q
        elif t == 'S':
            sapo += q

porccoelho = (coelho * 100) / contador
porcrato = (rato * 100) / contador
porcsapo = (sapo * 100) / contador

print(f'Total: {contador} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {porccoelho:.2f} %')
print(f'Percentual de ratos: {porcrato:.2f} %')
print(f'Percentual de sapos: {porcsapo:.2f} %')
