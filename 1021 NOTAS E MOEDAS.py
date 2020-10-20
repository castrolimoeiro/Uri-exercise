"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.
Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
Obs: Utilize ponto (.) para separar a parte decimal.
"""
# valor = float(input())
#
# notas = [100, 50, 20, 10, 5, 2]
# moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
#
#
# print('NOTAS: ')
# for n in notas:
#     divisor = valor // n
#     valor = valor - divisor * n
#     print(f'{int(divisor)} nota(s) de R$ {n:.2f} ')
#
# print('MOEDAS: ')
# for m in moedas:
#     divisor = valor // m
#     valor = valor - divisor * m
#     print(f'{int(divisor)} moeda(s) de R$ {m:.2f}')

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from math import ceil

# -*- coding: utf-8 -*-

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# print('NOTAS: ')
# for n in notas:
#     divisor = valor // n
#     print(f'{int(divisor)} nota(s) de R$ {n:.2f}')
#     valor -= divisor * n

divisor = (valor // n for n in notas)
print()


# print('MOEDAS: ')
# for m in moedas:
#     divisor = int(round(valor, 2) / m)
#     print(f'{int(divisor)} moeda(s) de R$ {m:.2f}')
#     valor -= divisor * m
