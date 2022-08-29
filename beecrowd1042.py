# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

lista = []
x, y, z = map(int, input().split()) 
lista.append(x)
lista.append(y)
lista.append(z)
lista.sort()
print(lista[0])
print(lista[1])
print(lista[2])
print()
print(x)
print(y)
print(z)
