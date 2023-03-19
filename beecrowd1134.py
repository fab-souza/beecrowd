"""
Tipo de Combustível

Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.

Exemplo de Entrada	
8                 MUITO OBRIGADO
1                 Alcool: 1
7                 Gasolina: 2
2                 Diesel: 0
2                 
4                 

"""

alcool = 0
gasolina = 0
diesel = 0
contador = 0

while contador < 1:
  combustivel = int(input())
  if combustivel == 1:
    alcool +=1

  elif combustivel == 2:
    gasolina +=1

  elif combustivel == 3:
    diesel +=1

  elif combustivel == 4:
    contador +=2

  else:
    continue

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))
