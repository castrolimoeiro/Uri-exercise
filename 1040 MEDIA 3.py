# -*- coding: utf-8 -*-

n1, n2, n3, n4 = input().split(' ')
n1 = float(n1) * 2
n2 = float(n2) * 3
n3 = float(n3) * 4
n4 = float(n4) * 1

media = (n1 + n2 + n3 + n4) / 10
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')

elif media < 5:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media_exame = (media + exame) / 2
    if media_exame >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_exame:.1f}')