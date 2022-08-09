# Este problema tem que ler o nome de um vendedor, seu salário fixo e o quanto ele vendeu no último mês. O vendedor recebe uma comissão de 15% sobre suas vendas, por isso seu salário final é a soma do salário fixo e a comissão.

nome = input()
salario_fixo = float(input())
vendas = float(input())
comissao = vendas * 0.15
salario_final = salario_fixo + comissao
print('TOTAL = R$ {:.2f}'.format(salario_final))

# Minha versão:
nome = input('Digite o nome d@ vendedor(a): ')
salario_fixo = float(input('Digite o valor do salário fixo: '))
vendas = float(input('Digite o valor das vendas: '))
comissao = vendas * 0.15
salario_final = salario_fixo + comissao
print('O salário será de = R$ {:.2f}'.format(salario_final))
