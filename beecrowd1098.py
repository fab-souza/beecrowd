"""
Sequencia IJ 4

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""

I = 0
J = 1
contador = 0
soma = 0

while I <= 2:
  print('I={} J={}'.format(I, J)) 
  J += 1
  contador += 1
  
  if contador == 3:
    soma = 0.2
    I += soma
    J -= 3
    J += soma
    contador = 0
