"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
"""

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

contador = 0
valor_total = 0

valores = [valor1, valor2, valor3, valor4, valor5, valor6]

for valor in valores:
  if valor > 0:
    contador = contador + 1
    valor_total = valor_total + valor
  else:
    continue

media = valor_total / contador
print('{} valores positivos'.format(contador))
print(media)
