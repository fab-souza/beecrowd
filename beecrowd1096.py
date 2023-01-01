"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""

I = 1
J = 7

while I <= 9:
  print('I={} J={}'.format(I, J))
  I += 0
  J -= 1
  if J == 4:
    I += 2
    J = 7
