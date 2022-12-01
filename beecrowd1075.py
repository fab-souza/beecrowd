"""

Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

Entrada
A entrada contém um valor inteiro N (N < 10000).

Saída
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

"""

entrada = int(input())
contador = 1

while contador < 10001:
  if contador % entrada == 2:
    print(contador)
  contador += 1
