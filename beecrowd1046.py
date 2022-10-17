# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

A, B = map(int, input().split()) 

if (B == A):
  print('O JOGO DUROU 24 HORA(S)')

elif (A < B):
  horas = B - A
  print('O JOGO DUROU {} HORA(S)'.format(horas))

else:
  horas = (A - 24)
  horas *= (-1)
  horas += B
  print('O JOGO DUROU {} HORA(S)'.format(horas))
