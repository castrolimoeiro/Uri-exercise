# -*- coding: utf-8 -*-

salario = float(input())

if 0 < salario <= 400:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'Novo salario: {novo_salario:.2f}\n'
          f'Reajuste ganho: {aumento:.2f}\n'
          f'Em percentual: 15 %')
elif 400 < salario <= 800:
    aumento = salario * 0.12
    novo_salario = salario + aumento
    print(f'Novo salario: {novo_salario:.2f}\n'
          f'Reajuste ganho: {aumento:.2f}\n'
          f'Em percentual: 12 %')
elif 800 < salario <= 1200:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'Novo salario: {novo_salario:.2f}\n'
          f'Reajuste ganho: {aumento:.2f}\n'
          f'Em percentual: 10 %')
elif 1200 < salario <= 2000:
    aumento = salario * 0.07
    novo_salario = salario + aumento
    print(f'Novo salario: {novo_salario:.2f}\n'
          f'Reajuste ganho: {aumento:.2f}\n'
          f'Em percentual: 7 %')
else:
    aumento = salario * 0.04
    novo_salario = salario + aumento
    print(f'Novo salario: {novo_salario:.2f}\n'
          f'Reajuste ganho: {aumento:.2f}\n'
          f'Em percentual: 4 %')
