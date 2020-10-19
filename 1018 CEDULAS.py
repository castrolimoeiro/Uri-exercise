"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""

valor = int(input())


nota_100 = valor // 100
valor = valor - (nota_100 * 100)

nota_50 = valor // 50
valor = valor - (nota_50 * 50)

nota_20 = valor // 20
valor = valor - (nota_20 * 20)

nota_10 = valor // 10
valor = valor - (nota_10 * 10)

nota_5 = valor // 5
valor = valor - (nota_5 * 5)

nota_2 = valor // 2
valor = valor - (nota_2 * 2)

nota_1 = valor


print(nota_100)
print(nota_50)
print(nota_20)
print(nota_10)
print(nota_5)
print(nota_2)
print(nota_1)
