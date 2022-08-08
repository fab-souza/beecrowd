# Este problema pedia para ler 4 valores inteiros (A, B, C e D), calcular e mostrar a diferença do produto de A e B pelo produto de C e D

A = int(input())
B = int(input())
C = int(input())
D = int(input())
diferenca = A * B - C * D
print('DIFERENCA = {}'.format(diferenca))

# Minha versão mais 'amigável'

A = int(input('Digite um número inteiro: '))
B = int(input('Digite outro número inteiro: '))
C = int(input('Digite o 3º número inteiro: '))
D = int(input('Digite o último número inteiro: '))
diferenca = A * B - C * D
print('A diferença entre (A * B) e (C * D) = {}'.format(diferenca))
