# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A,
# e a soma de C com D for maior que a soma de A e B e se C e D, 
# ambos, forem positivos 
# e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

A, B, C, D = map(int, input().split()) 
if (B > C and D > A):
  cd = C + D
  ab = A + B
  if (cd > ab and ab > 0 and cd > 0):
    restoA = A % 2
    if (restoA == 0):
      print('Valores aceitos') 
    else:
      print('Valores nao aceitos')
  else:
    print('Valores nao aceitos')
else:
  print('Valores nao aceitos')
  
# Minha versão:

A, B, C, D = map(int, input().split()) 
if (B > C and D > A):
  print('B é maior do que C e D é maior do que A.')
  cd = C + D
  ab = A + B
  if (cd > ab and ab > 0 and cd > 0):
    print('A soma de C e D é maior do que A com B.')
    print('E os valores das somas são positivos')
    restoA = A % 2
    if (restoA == 0):
      print('Valores aceitos') 
    else:
      print('Valores nao aceitos')
  else:
    print('Valores nao aceitos')
else:
  print('Valores nao aceitos')
