# Este problema pedia para calcular a distância entre dois pontos, através da leitura de duas coordenadas: p1(x1, y1) e p2(x2, y2)

import math
x1, y1 = map(float, input().split()) 
x2, y2 = map(float, input().split()) 
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('{:.4f}'.format(distancia))

# Minha versão mais amigável:

import math
x1, y1 = map(float, input('Digite as coordenadas do ponto 1: ').split()) 
x2, y2 = map(float, input('Digite as coordenadas do ponto 2: ').split()) 
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('A distância entre os pontos é de {:.4f}'.format(distancia))
