"""
Múltiplos de 13

Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

Exemplo
100       13954
200       

"""

x = int(input())
y = int(input())

soma = 0

if (x > y):
  for valor in range(y, x + 1):
    if valor % 13 != 0:
      soma += valor
    else:
       continue
  
  print(soma)

else:
  for valor in range(x, y + 1):
    if valor % 13 != 0:
      soma += valor
    else:
       continue
    
  print(soma)
