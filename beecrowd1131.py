"""
Grenais

A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

Exemplo
3 2       Novo grenal (1-sim 2-nao)
1         Novo grenal (1-sim 2-nao)
2 3       Novo grenal (1-sim 2-nao)
1         3 grenais
3 1       Inter:2
2         Gremio:1
          Empates:0
          Inter venceu mais

"""

contagem = 0
grenal = 1
gremio = 0
inter = 0
empate = 0

while contagem < 1000:
  inter_saldo, gremio_saldo = map(int, input().split())

  if gremio_saldo > inter_saldo:
    gremio += 1

  elif gremio_saldo == inter_saldo:
    empate += 1

  else:
    inter += 1

  mais_um = int(input('Novo grenal (1-sim 2-nao)\n'))
  if mais_um == 1:
    grenal += 1
    continue

  else:
    break

print('{} grenais'.format(grenal))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))
if gremio > inter:
  print('Gremio venceu mais')
else:
  print('Inter venceu mais')
