"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.
"""

valor_entrada = int(input())

contador = 0
dentro = 0
fora = 0

while contador < valor_entrada:
  valor = int(input())
  contador += 1
  if (valor >= 10 and valor <= 20):
    dentro += 1

  else:
    fora += 1
    
print('{} in'.format(dentro))
print('{} out'.format(fora))

