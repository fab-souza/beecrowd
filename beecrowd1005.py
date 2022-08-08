# Este problema pede para calcular a média de duas notas de um aluno, a 1ª nota tem peso 3,5 e a 2ª 7,5

A = float(input())
B = float(input())
A = A * 3.5
B = B * 7.5
media = (A + B) / 11
print('MEDIA = {:.5f}'.format(media))

# Eu só deixaria os inputs mais explicativos sobre o que eles se tratam:

A = float(input('Digite a 1ª nota d@ alun@: '))
B = float(input('Digite a 2ª nota: '))
A = A * 3.5
B = B * 7.5
media = (A + B) / 11
print('A média obtida foi = {:.5f}'.format(media))
