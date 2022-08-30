# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

lista = []
x, y, z = map(float, input().split()) 
lista.append(x)
lista.append(y)
lista.append(z)
lista.sort(reverse=True)
A = lista[0]
B = lista[1]
C = lista[2]

if (A >= B+C):
  print('NAO FORMA TRIANGULO')
  exit()

if (A**2 == (B**2) + (C**2)):
  print('TRIANGULO RETANGULO')
elif (A**2 > B**2 + C**2):
  print('TRIANGULO OBTUSANGULO')
elif (A**2 < B**2 + C**2):
  print('TRIANGULO ACUTANGULO')

if (A == B == C):
  print('TRIANGULO EQUILATERO')
elif (A == B or A == C or B == C):
  print('TRIANGULO ISOSCELES')
