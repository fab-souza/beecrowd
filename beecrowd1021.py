# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

valor = float(input())
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
# moedas
valor_um = resto // 1
resto = resto % 1
valor_moeda_cinquenta = resto // 0.50
resto = resto % 0.50
valor_moeda_vinte_cinco = resto // 0.25
resto = resto % 0.25
valor_moeda_dez = resto // 0.10
resto = resto % 0.10
valor_moeda_cinco = resto // 0.05
resto = resto % 0.05
valor_moeda_um = resto // 0.01
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(valor_cem)))
print('{} nota(s) de R$ 50.00'.format(int(valor_cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(valor_vinte)))
print('{} nota(s) de R$ 10.00'.format(int(valor_dez)))
print('{} nota(s) de R$ 5.00'.format(int(valor_cinco)))
print('{} nota(s) de R$ 2.00'.format(int(valor_dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(valor_um)))
print('{} moeda(s) de R$ 0.50'.format(int(valor_moeda_cinquenta)))
print('{} moeda(s) de R$ 0.25'.format(int(valor_moeda_vinte_cinco)))
print('{} moeda(s) de R$ 0.10'.format(int(valor_moeda_dez)))
print('{} moeda(s) de R$ 0.05'.format(int(valor_moeda_cinco)))
print('{} moeda(s) de R$ 0.01'.format(int(valor_moeda_um)))


# Por algum motivo, o Beecrowd não está aceitando esta resposta :/
