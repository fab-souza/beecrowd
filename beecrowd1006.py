# Problema é parecido com o anterior, porém agora são 3 notas, com peso 2, 3 e 5

A = float(input())
B = float(input())
C = float(input())
A = A * 2
B = B * 3
C = C * 5
media = (A + B + C) / 10
print('MEDIA = {:.1f}'.format(media))

# Novamente, eu só deixaria o input mais explicativo:

A = float(input('Digite a 1ª nota (peso 2):'))
B = float(input('Digite a 2ª nota (peso 3):'))
C = float(input('Digite a última nota (peso 5):'))
A = A * 2
B = B * 3
C = C * 5
media = (A + B + C) / 10
print('A média obtida foi = {:.1f}'.format(media))
