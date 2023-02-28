"""
Resto da Divisão

Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Exemplo
10       12
18       13
         17

"""

x = int(input())
y = int(input())

if (x > y):
  for valor in range(y, x):
    if (valor % 5 == 2 or valor % 5 == 3):
      print(valor)
    else:
       continue

else:
  for valor in range(x, y):
    if (valor % 5 == 2 or valor % 5 == 3):
      print(valor)
    else:
       continue
