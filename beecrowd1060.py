"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
"""

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

contador = 0

valores = [valor1, valor2, valor3, valor4, valor5, valor6]

for valor in valores:
  if valor > 0:
    contador = contador + 1
  else:
    continue

print('{} valores positivos'.format(contador))


# Minha verssão:

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))
valor3 = float(input('Digite um valor: '))
valor4 = float(input('Digite um valor: '))
valor5 = float(input('Digite um valor: '))
valor6 = float(input('Digite o último valor: '))

contador = 0

valores = [valor1, valor2, valor3, valor4, valor5, valor6]

for valor in valores:
  if valor > 0:
    contador = contador + 1
  else:
    continue

print('Há {} valores positivos'.format(contador))
