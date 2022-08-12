# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

valor = int(input())
valor_cem = valor // 100
resto = valor % 100
valor_cinquenta = resto // 50
resto = resto % 50
valor_vinte = resto // 20
resto = resto % 20
valor_dez = resto // 10
resto = resto % 10
valor_cinco = resto // 5
resto = resto % 5
valor_dois = resto // 2
resto = resto % 2
valor_um = resto // 1
print('{}'.format(valor))
print('{} nota(s) de R$ 100,00'.format(valor_cem))
print('{} nota(s) de R$ 50,00'.format(valor_cinquenta))
print('{} nota(s) de R$ 20,00'.format(valor_vinte))
print('{} nota(s) de R$ 10,00'.format(valor_dez))
print('{} nota(s) de R$ 5,00'.format(valor_cinco))
print('{} nota(s) de R$ 2,00'.format(valor_dois))
print('{} nota(s) de R$ 1,00'.format(valor_um))

# Minha versão:

valor = int(input('Digite um valor inteiro: '))
valor_cem = valor // 100
resto = valor % 100
valor_cinquenta = resto // 50
resto = resto % 50
valor_vinte = resto // 20
resto = resto % 20
valor_dez = resto // 10
resto = resto % 10
valor_cinco = resto // 5
resto = resto % 5
valor_dois = resto // 2
resto = resto % 2
valor_um = resto // 1
print('Para o valor {}'.format(valor))
print('Serão {} nota(s) de R$ 100,00'.format(valor_cem))
print('Serão {} nota(s) de R$ 50,00'.format(valor_cinquenta))
print('Serão {} nota(s) de R$ 20,00'.format(valor_vinte))
print('Serão {} nota(s) de R$ 10,00'.format(valor_dez))
print('Serão {} nota(s) de R$ 5,00'.format(valor_cinco))
print('Serão {} nota(s) de R$ 2,00'.format(valor_dois))
print('Serão {} nota(s) de R$ 1,00'.format(valor_um))
