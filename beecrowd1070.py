"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

"""

valor1 = int(input())

contador = 0

if (valor1 % 2 == 0):
  valor1 = valor1 + 1
  while contador < 6:
    print(valor1)
    contador += 1
    valor1 += 2

else:
  while contador < 6:
    print(valor1)
    valor1 += 2
    contador += 1
