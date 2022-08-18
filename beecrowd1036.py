# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

import math

a, b, c = map(float, input().split()) 
d = (b**2) - (4*a*c)
if (a == 0 or d < 0):
  print('Impossivel calcular')
else:
  x1 = (-b + math.sqrt(d)) / (2 * a)
  print('R1 = {:.5f}'.format(x1))
  x2 = (-b - math.sqrt(d)) / (2 * a)
  print('R2 = {:.5f}'.format(x2))
  
# Minha versão mais amigável:

import math

a, b, c = map(float, input('Digite três valores com uma casa decimal: ').split()) 
d = (b**2) - (4*a*c)
if (a == 0 or d < 0):
  print('Impossivel calcular. Pois o 1º valor é zero ou delta é um valor negativo :/')
else:
  x1 = (-b + math.sqrt(d)) / (2 * a)
  print('x1 = {:.5f}'.format(x1))
  x2 = (-b - math.sqrt(d)) / (2 * a)
  print('x2 = {:.5f}'.format(x2))
