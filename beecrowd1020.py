# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

dias = int(input())
anos = dias // 365
resto = dias % 365
meses = resto // 30
resto = resto % 30
dia = resto 
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dia))

# Minha versão:

dias = int(input('Digite um valor inteiro, representando sua idade em dias: '))
anos = dias // 365
resto = dias % 365
meses = resto // 30
resto = resto % 30
dia = resto 
print('Você tem {} ano(s),'.format(anos))
print('{} mes(es) e'.format(meses))
print('{} dia(s) de idade.'.format(dia))
