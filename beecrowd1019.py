# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

valor = int(input())
hora = valor // 3600
resto = valor % 3600
minuto = resto // 60
segundo = resto % 60
print('{}:{}:{}'.format(hora, minuto, segundo))

# Minha versão:

valor = int(input('Digite um valor inteiro: '))
hora = valor // 3600
resto = valor % 3600
minuto = resto // 60
segundo = resto % 60
print('Serão {} horas {} minutos e {} segundos.'.format(hora, minuto, segundo))
