# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

A, B = map(int, input().split()) 

if (B < A):
  if (A % B == 0):
    print('Sao Multiplos')
  else:
    print('Nao sao Multiplos')

else:
  if (B % A == 0):
    print('Sao Multiplos')
  else:
    print('Nao sao Multiplos')
