"""
1101 - Sequência de Números e Soma

Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

5 2    2 3 4 5 Sum=14
6 3    3 4 5 6 Sum=18
5 0

"""

contador = 0

while (contador < 1000):
  M, N = map(int, input().split())
  soma = 0
  if (M > 0 and N > 0):
    if (M < N):
      for numero in range(M, N+1):
        soma += numero
        print(numero, end = ' ')
      print('Sum={}'.format(soma))
      contador += 1
    
    else:
      for numero in range(N, M+1):
        soma += numero
        print(numero, end = ' ')
      print('Sum={}'.format(soma))
      contador += 1
  
  else:
    break
