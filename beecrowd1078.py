"""

Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N

Entrada
A entrada contém um valor inteiro N (2 < N < 1000).

Saída
Imprima a tabuada de N, conforme o exemplo fornecido.

"""

valor = int(input())
contador = 1

while contador < 11:
  resultado = contador * valor
  print('{} x {} = {}'.format(contador, valor, resultado))
  contador += 1
