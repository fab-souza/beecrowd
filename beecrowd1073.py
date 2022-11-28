"""

Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

"""

entrada = int(input())

if entrada % 2 == 0:
  for valor in range (2, entrada+1, 2):
    quadrado = valor ** 2
    print('{}^2 = {}'.format(valor, quadrado))

    
else:
  contador = 2
  while contador < entrada:
    quadrado = contador ** 2
    print('{}^2 = {}'.format(contador, quadrado))
    contador += 2
