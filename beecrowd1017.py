# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

tempo = int(input())
velocidade_media = int(input())
distancia = tempo * velocidade_media
litros = distancia / 12
print('{:.3f}'.format(litros))

# Minha versão:

tempo = int(input('Digite o tempo da viagem: '))
velocidade_media = int(input('Digite a velocidade média feita durante a viagem:'))
distancia = tempo * velocidade_media
litros = distancia / 12
print('Serão necessários {:.3f} litros'.format(litros))
