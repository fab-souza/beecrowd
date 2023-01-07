"""
Senha Fixa

Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.

Exemplo:
2200                  Senha Invalida
1020                  Senha Invalida
2022                  Senha Invalida
2002                  Acesso Permitido

"""

contador = 0
senha = 2002

while (contador < 1000):
  tentativa = int(input())
  if (senha == tentativa):
    print('Acesso Permitido')
    break

  else:
    print('Senha Invalida')
    contador += 1
    
 # Minha versão:

contador = 0
senha = 2002

while (contador < 1000):
  tentativa = int(input('Digite a senha: '))
  if (senha == tentativa):
    print('Acesso Permitido')
    break

  else:
    print('Senha Invalida')
    contador += 1
