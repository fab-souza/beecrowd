# Este problema pedia para calcular o volume de uma esfera

raio = int(input())
pi = 3.14159
volume = (4/3) * pi * (raio**3)
print('VOLUME = {:.3f}'.format(volume))

# Minha versão só teria uma mensagem mais amigável no input:

raio = int(input('Digite o valor do raio de esfera: '))
pi = 3.14159
volume = (4/3) * pi * (raio**3)
print('O volume da esfera = {:.3f}'.format(volume))
