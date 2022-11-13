"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
"""

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())

contador = 0

valores = [valor1, valor2, valor3, valor4, valor5]

for valor in valores:
  if (valor % 2 == 0):
    contador = contador + 1
  else:
    continue

print('{} valores pares'.format(contador))
