# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# Código  Produto          Preço
# 1       Cachorro quente  R$4,00
# 2       X-salada         R$4,50
# 3       X-bacon          R$5,00
# 4       Torrada simples  R$2,00
# 5       Refrigerante     R$1,50

item, quantidade = map(int, input().split()) 

if (item == 1):
  preco = quantidade * 4.00
  print('Total: R$ {:.2f}'.format(preco))
elif (item == 2):
  preco = quantidade * 4.50
  print('Total: R$ {:.2f}'.format(preco)) 
elif (item == 3):
  preco = quantidade * 5.00
  print('Total: R$ {:.2f}'.format(preco))
elif (item == 4):
  preco = quantidade * 2.00
  print('Total: R$ {:.2f}'.format(preco))
else:
  preco = quantidade * 1.50
  print('Total: R$ {:.2f}'.format(preco))
  
  # Minha versão:
  
  print('Olá, temos os seguintes produtos:')
  print('Código  Produto          Preço')
  print('1       Cachorro quente  R$4,00')
  print('2       X-salada         R$4,50')
  print('3       X-bacon          R$5,00')
  print('4       Torrada simples  R$2,00')
  print('5       Refrigerante     R$1,50')
  
  item, quantidade = map(int, input('Digite o código do produto e a quantidade ').split()) 

if (item == 1):
  preco = quantidade * 4.00
  print('Total: R$ {:.2f}'.format(preco))
elif (item == 2):
  preco = quantidade * 4.50
  print('Total: R$ {:.2f}'.format(preco)) 
elif (item == 3):
  preco = quantidade * 5.00
  print('Total: R$ {:.2f}'.format(preco))
elif (item == 4):
  preco = quantidade * 2.00
  print('Total: R$ {:.2f}'.format(preco))
else:
  preco = quantidade * 1.50
  print('Total: R$ {:.2f}'.format(preco))
