'''
Faça um programa que leia os nomes recebidos e sorteie uma ordem com esses nomes.
'''

from random import shuffle

nome = input('Digite o primeiro nome: ')
nome_1 = input('Digite o segundo nome: ')
nome_2 = input('Digite o terceiro nome: ')
nome_3 = input('Digite o quarto nome: ')

lista = [nome, nome_1, nome_2, nome_3]

shuffle(lista)

print('A ordem sorteada foi: {}'.format(lista))