# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

# Perimetro = XX.X

# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

# Area = XX.X

A, B, C = map(float, input().split()) 

if (A < B+C and B < A+C and C < A+B):
  perimetro = A+B+C
  print('Perimetro = {:.1f}'.format(perimetro))

else:
  area = ((A+B)*C)/2
  print('Area = {:.1f}'.format(area))
