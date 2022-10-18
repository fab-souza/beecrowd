# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

A, B, C, D = map(int, input().split()) 

if (A < C and B < D):
  horas = C - A
  minuto = D - B
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minuto))

elif (A < C and B > D):
  horas = C - A
  minuto = (D + 60) - B
  #horas -= 1
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minuto))

elif (A > C and B < D):
  minuto = D - B
  horas = (C + 24) - A
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minuto))

elif (A > C and B > D):
  horas = (C + 24) - A
  minuto = (D + 60) - B
  horas -= 1
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minuto))

else:
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
