"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
"""

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())

par = 0
impar = 0
positivo = 0
negativo = 0

valores = [valor1, valor2, valor3, valor4, valor5]

for valor in valores:
  if (valor % 2 == 0):
    par = par + 1
    if (valor > 0):
      positivo += 1
      
    elif (valor < 0):
      negativo += 1
      
    else:
      continue

  elif (valor % 2 != 0):
    impar += 1
    if (valor > 0):
      positivo += 1

    elif (valor < 0):
      negativo += 1
      
    else:
      continue

  else:
    continue

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
