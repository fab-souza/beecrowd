# Problema simples, que pedia o raio de uma circunferência e o código devolvia a área do circulo, com precisão de quatro casas decimais.
# Obs.: n representa pi = 3,14159

raio = float(input())
n = 3.14159
a = n * (raio ** 2)
print('A={:.4f}'.format(a))

# Neste problema, eu não mudaria muita coisa, só adicionaria uma mensagem solicitando a digitação do número:

raio = float(input('Digite o raio da circunferência:'))
pi = 3.14159
a = pi * (raio ** 2)
print('Área = {:.4f}'.format(a))
