"""

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

"""

valor1 = int(input())
valor2 = int(input())

contador = 0

if (valor1 > valor2):
  if (valor2 % 2 != 0):
    valor2 +=1
  if (valor1 % 2 == 0):
    valor1 +=1
  for i in range(valor2, valor1):
    if (i % 2 != 0):
      contador = contador + i  

elif (valor1 < valor2):
  if (valor1 % 2 != 0):
    valor1 +=1
  for i in range(valor1, valor2):
    if (i % 2 != 0):
      contador = contador + i

else:
  continue

print(contador)
