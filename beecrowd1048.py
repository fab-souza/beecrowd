# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

# Salário	Percentual de Reajuste
# 0 - 400.00           | 15%
# 400.01 - 800.00      | 12%
# 800.01 - 1200.00     | 10%
# 1200.01 - 2000.00    | 7%
# Acima de 2000.00     | 4%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

salario = float(input())

if (salario >= 0 and salario <= 400.00):
  percentual = 15
  novo_salario = salario * 1.15
  reajuste = novo_salario - salario
  print('Novo salario: {:.2f}'.format(novo_salario))
  print('Reajuste ganho: {:.2f}'.format(reajuste))
  print('Em percentual: {} %'.format(percentual))

elif (salario >= 400.01 and salario <= 800.00):
  percentual = 12
  novo_salario = salario * 1.12
  reajuste = novo_salario - salario
  print('Novo salario: {:.2f}'.format(novo_salario))
  print('Reajuste ganho: {:.2f}'.format(reajuste))
  print('Em percentual: {} %'.format(percentual))

elif (salario >= 800.01 and salario <= 1200.00):
  percentual = 10
  novo_salario = salario * 1.10
  reajuste = novo_salario - salario
  print('Novo salario: {:.2f}'.format(novo_salario))
  print('Reajuste ganho: {:.2f}'.format(reajuste))
  print('Em percentual: {} %'.format(percentual))
  
elif (salario >= 1200.01 and salario <= 2000.00):
  percentual = 7
  novo_salario = salario * 1.07
  reajuste = novo_salario - salario
  print('Novo salario: {:.2f}'.format(novo_salario))
  print('Reajuste ganho: {:.2f}'.format(reajuste))
  print('Em percentual: {} %'.format(percentual))

else:
  percentual = 4
  novo_salario = salario * 1.04
  reajuste = novo_salario - salario
  print('Novo salario: {:.2f}'.format(novo_salario))
  print('Reajuste ganho: {:.2f}'.format(reajuste))
  print('Em percentual: {} %'.format(percentual))
