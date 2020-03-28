'''
Faça um programa leia e sorteie os nomes digitados.
'''

from random import choice

nome = input('Digite o primeiro nome: ')
nome_1 = input('Digite o segundo nome: ')
nome_2 = input('Digite o terceiro nome: ')
nome_3 = input('Digite o quarto nome: ')

lista = [nome, nome_1, nome_2, nome_3]

sorteio = choice(lista)

print('O nome sorteado foi {}'.format(sorteio))