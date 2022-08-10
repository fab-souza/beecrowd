# Este problema pedia para calcular o consumo médio de um automóvel, ao ler a distância total percorrida (em Km) e o total de combustível gasto (em litros).

X = int(input())
Y = float(input())
consumo = X / Y
print('{:.3f} km/l'.format(consumo))

# Minha versão:

X = int(input('Digite a distância percorrida (em Km)'))
Y = float(input('Digite o total de combustível gasto (em litros)'))
consumo = X / Y
print('O consumo médio foi de {:.3f} km/l'.format(consumo))
