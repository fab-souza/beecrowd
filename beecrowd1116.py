"""
Dividindo X por Y

Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

Exemplo

3         -1.5
3 -2      divisao impossivel
-8 0      0.0
0 8     
"""

quantidade = int(input())
contador = 0

while (contador < quantidade):
  x, y = map(int, input().split())
  resultado = 0
  if (y == 0):
    print('divisao impossivel')
    contador += 1
    
  else:
    resultado = x / y
    print(resultado)
    contador += 1
    
#================== Minha versão =====================

quantidade = int(input('Digite a quantidade de operações que quer fazer: '))
contador = 0

while (contador < quantidade):
  x, y = map(int, input('Digite o numerador e denominador: ').split())
  resultado = 0
  if (y == 0):
    print('divisao impossivel')
    contador += 1
    
  else:
    resultado = x / y
    print(resultado)
    contador += 1
