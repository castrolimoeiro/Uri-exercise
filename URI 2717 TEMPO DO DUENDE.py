tempo = int(input())
a, b = input().split()
total = int(a) + int(b)
if tempo >= total:
    print('Farei hoje!')
else:
    print('Deixa para amanha!')
