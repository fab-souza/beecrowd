"""
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.
"""

repeticao = int(input())
contador = 0

while contador < repeticao:
  A, B, C = map(float, input().split())
  primeiro = A * 2
  segundo = B * 3
  terceiro = C * 5
  media_ponderada = (primeiro + segundo + terceiro) / 10
  print('{:.1f}'.format(media_ponderada))
  contador += 1
