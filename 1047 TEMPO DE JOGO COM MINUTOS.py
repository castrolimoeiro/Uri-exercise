# -*- coding: utf-8 -*-

h_inicial, m_inicial, h_final, m_final = input().split(' ')

h_inicial = int(h_inicial) * 60
m_inicial = int(m_inicial)
tempoini = h_inicial + m_inicial

h_final = int(h_final) * 60
m_final = int(m_final)
tempofim = h_final + m_final

if tempoini >= tempofim:
    duracao = 1440 - tempoini + tempofim
else:
    duracao = tempofim - tempoini

hora = duracao // 60
minuto = duracao % 60

print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
