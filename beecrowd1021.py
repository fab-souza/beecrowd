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
print('{:.0f} nota(s) de R$ 100.00'.format(valor_cem))
print('{:.0f} nota(s) de R$ 50.00'.format(valor_cinquenta))
print('{:.0f} nota(s) de R$ 20.00'.format(valor_vinte))
print('{:.0f} nota(s) de R$ 10.00'.format(valor_dez))
print('{:.0f} nota(s) de R$ 5.00'.format(valor_cinco))
print('{:.0f} nota(s) de R$ 2.00'.format(valor_dois))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(valor_um))
print('{:.0f} moeda(s) de R$ 0.50'.format(valor_moeda_cinquenta))
print('{:.0f} moeda(s) de R$ 0.25'.format(valor_moeda_vinte_cinco))
print('{:.0f} moeda(s) de R$ 0.10'.format(valor_moeda_dez))
print('{:.0f} moeda(s) de R$ 0.05'.format(valor_moeda_cinco))
print('{:.0f} moeda(s) de R$ 0.01'.format(valor_moeda_um))


# Por algum motivo, o Beecrowd não está aceitando esta resposta :/
# E há muitas dúvidas, no fórum da plataforma, sobre a resposta do problema estar errada.
