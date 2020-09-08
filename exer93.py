"""
Faça um programa em Python que leia dados do usuário (nome, sobrenome, idade)
adicione em uma lista e imprima seus elementos na tela.
"""

lista = []
try:
    lista.append(input('Digite seu nome: '))
    lista.append(input('Digite seu sobrenome: '))
    lista.append(int(input('Digite sua idade: ')))
except ValueError:
    print('A idade deve ser um número inteiro.')
    exit()
print(lista)
