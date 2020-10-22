# -*- coding: utf-8 -*-

a, b = input().split(' ')
a = int(a)
b = int(b)

if a >= b:
    duracao = 24 - a + b
    print(f'O JOGO DUROU {duracao} HORA(S)')
else:
    duracao = b - a
    print(f'O JOGO DUROU {duracao} HORA(S)')
