"""
Soma de Ímpares Consecutivos II

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
"""

casos_de_testes = int(input())
vezes = 0

while vezes < casos_de_testes:
  valor1, valor2 = map(int, input().split())
  contador = 0
  
  if (valor1 > valor2):
    if (valor2 % 2 != 0):
      valor2 +=1
    if (valor1 % 2 == 0):
      valor1 +=1
    for i in range(valor2, valor1):
      if (i % 2 != 0):
        contador = contador + i  
  
  else:
    if (valor1 % 2 != 0):
      valor1 +=1
    for i in range(valor1, valor2):
      if (i % 2 != 0):
        contador = contador + i

  print('{}'.format(contador))
  vezes += 1
