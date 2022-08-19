# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

a = float(input())
if (a > 75.00 and a <= 100):
  print('Intervalo (75,100]')
elif (a <= 75.00 and a > 50.00001):
  print('Intervalo (50,75]') 
elif (a <= 50.00 and a > 25.00001):
  print('Intervalo (25,50]')
elif (a <= 25.0000 and a >= 0.00):
  print('Intervalo [0,25]')
else:
  print('Fora de intervalo')
  
# Minha versão:

a = float(input('Digite um valor com duas casas decimais: '))
if (a > 75.00 and a <= 100):
  print('Intervalo (75,100]')
elif (a <= 75.00 and a > 50.00001):
  print('Intervalo (50,75]') 
elif (a <= 50.00 and a > 25.00001):
  print('Intervalo (25,50]')
elif (a <= 25.0000 and a >= 0.00):
  print('Intervalo [0,25]')
else:
  print('Fora de intervalo')
