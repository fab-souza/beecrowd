# Este problema simulava o caixa de uma loja. Ele pedia para ler 6 valores, 3 de cada vez. Os dois primeiros, seriam do tipo 'int' enquanto o último seria do tipo 'float'. O primeiro valor é referente ao código do produto, o segundo valor é referente a quantidade deste produto que está sendo comprada e o último é refente ao valor do produto. Ao final, deveria apresentar o valor total da compra, somando o quanto deu em cada produto.

produto1, quantidade1, valor1 = input().split()
produto1 = int(produto1)
quantidade1 = int(quantidade1)
valor1 = float(valor1)
produto2, quantidade2, valor2 = input().split()
produto2 = int(produto2)
quantidade2 = int(quantidade2)
valor2 = float(valor2)
valor_primeiro_produto = quantidade1 * valor1
valor_segundo_produto = quantidade2 * valor2
valor_final = valor_primeiro_produto + valor_segundo_produto
print('VALOR A PAGAR: R$ {:.2f}'.format(valor_final))

# Minha versão:

produto1, quantidade1, valor1 = input('Digite o código do produto, a sua quantidade e seu preço: ').split()
produto1 = int(produto1)
quantidade1 = int(quantidade1)
valor1 = float(valor1)
produto2, quantidade2, valor2 = input('Digite o código do produto, a sua quantidade e seu preço: ').split()
produto2 = int(produto2)
quantidade2 = int(quantidade2)
valor2 = float(valor2)
valor_primeiro_produto = quantidade1 * valor1
valor_segundo_produto = quantidade2 * valor2
valor_final = valor_primeiro_produto + valor_segundo_produto
print('VALOR A PAGAR: R$ {:.2f}'.format(valor_final))
