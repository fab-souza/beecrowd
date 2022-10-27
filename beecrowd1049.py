# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

estrutura1 = input()
estrutura2 = input()
estrutura3 = input()


if estrutura1 == 'vertebrado':
  # ave ou mamífero
  if estrutura2 == 'ave':
    # carnívoro ou onivoro
    if estrutura3 == 'carnivoro':
      print('aguia')
    else:
      print('pomba')
  else: #mamífero
    if estrutura3 == 'onivoro':
      print('homem')
    else: #herbivoro
      print('vaca')
  
  
else: #invertebrado
  # inseto ou anelídeo
  if estrutura2 == 'inseto':
    # hematofago ou herbivoro
    if estrutura3 == 'hematofago':
      print('pulga')
    else: #herbivoro
      print('lagarta')
  
  else: #anelídeo
    # hematofago ou onívoro
    if estrutura3 == 'hematofago':
      print('sanguessuga')
    else: #onívoro
      print('minhoca')
