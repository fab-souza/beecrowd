# Este problema pedia para ler 2 números inteiros, referentes ao número de um funcionário e da quantidade de horas que ele trabalhou no mês. O 3º número, é o valor da hora trabalhada. Depois, deveria calcular o salário que o funcionário receberia e apresentar o número do funcionário junto com o salário.

number = int(input())
horas = int(input())
salario = float(input())
salary = horas * salario
print('NUMBER = {}'.format(number))
print('SALARY = U${:.2f}'.format(salary))

# Minha versão:

number = int(input('Digite o número do funcionário: '))
horas = int(input('Digite o número de horas trabalhadas: '))
salario = float(input('Digite o valor da hora trabalhada: '))
salary = horas * salario
print('Número do funcionário = {}'.format(number))
print('O salário deste mês será = U$ {:.2f}'.format(salary))
