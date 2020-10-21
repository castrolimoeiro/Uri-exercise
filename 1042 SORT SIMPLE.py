"""
Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida,
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""

a, b, c = input().split(' ')
lista = []
lista.append(int(a))
lista.append(int(b))
lista.append(int(c))
lista2 = lista.copy()

lista.sort()
for c in lista:
    print(c)

print()

for c in lista2:
    print(c)
