"""
Faça um programa em Python que receba do usuário quinze números inteiros e
verifique a existência de elementos iguais a 30, mostrando as posições na
lista em que apareceram.
"""

lista = []

for i in range(1, 16):
    lista.append(int(input(f'Digite o {i}º número: ')))
    
for i in range(len(lista)):
    if lista[i] == 30:
        print(25 * '=')
        print(f'Posição: {i + 1}')
