# Este problema receberia 3 valores para calcular a área de diversas figuras planas:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

A, B, C = map(float, input().split()) 
pi = 3.14159
triangulo = A * C / 2
circulo = (C ** 2) * pi
trapezio = (A + B) * C / 2
quadrado = B * B
retangulo = A * B
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
