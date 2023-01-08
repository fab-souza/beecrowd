"""
1115 - Quadrante

Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

Exemplo:
2 2                primeiro
3 -2               quarto
-8 -1              terceiro 
-7 1               segundo
0 2                

"""
contador = 0

while (contador < 1000):
  x, y = map(float, input().split())
  if (x == 0 or y == 0):
    break

  elif (x > 0 and y > 0):
    print('primeiro')
    contador += 1

  elif (x > 0 and y < 0):
    print('quarto')
    contador += 1

  elif (x < 0 and y > 0):
    print('segundo')
    contador += 1
    
  else:
    print('terceiro')
    contador += 1
 
