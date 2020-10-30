
cpf = input()
a = cpf[0:3]
b = cpf[4:7]
c = cpf[8:11]
d = cpf[12:]
lista = [a, b, c, d]

for item in lista:
    print(item)
