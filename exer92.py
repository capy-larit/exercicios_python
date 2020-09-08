"""
Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa em
Python que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
"""

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
listaPares = []
somaNegativos = []
soma = 0


for i in lista:
    soma += i
    if i % 2 == 0:
        listaPares.append(i)
    if i < 0:
        somaNegativos.append(i)
media = soma / len(lista)

print(f'Maior: {max(lista)}\nMenor: {min(lista)}')
print(f'Pares: {listaPares}')
print(f'Ocorrências do primeiro número: {lista.count(lista[0])}')
print(f'Média: {media}\nNegativos: {somaNegativos}')
