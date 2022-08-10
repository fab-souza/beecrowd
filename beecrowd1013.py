# Este problema pedia para ler 3 números e devolver o maior valor:

A, B, C = map(int, input().split()) 
Mab = (A + B + abs(A - B)) / 2
Mabc = (Mab + C + abs(Mab - C)) / 2
Mabc = int(Mabc)
print('{} eh o maior'.format(Mabc))

# Minha versão:

A, B, C = map(int, input('Digite 3 valores: ').split()) 
Mab = (A + B + abs(A - B)) / 2
Mabc = (Mab + C + abs(Mab - C)) / 2
Mabc = int(Mabc)
print('{} é o maior'.format(Mabc))
