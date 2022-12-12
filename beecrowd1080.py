"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
"""

contador = 0
entrada = 0
posicao = 1
dado = {'chave' : 0, 'valor' : 0}

while contador < 100:
  valor = int(input())
  if valor > entrada:
    entrada = valor
    dado.update(chave = 'entrada', valor = 'posicao')
  posicao += 1
  contador += 1

print(dado['chave'])
print(dado['valor'])
