'''
Escreva um programa em Python que receba 3 números reais e mostre-os na tela em ordem decrescente. 

>>> Considere que o usuário digitará 3 números diferentes.
'''


numero = float(input('Digite o primeiro número: '))
numero_1 = float(input('Digite o segundo número: '))
numero_2 = float(input('Digite o terceiro número: '))

lista = [numero, numero_1, numero_2]

print('A ordem decrescente é {}'.format(sorted(lista, reverse = True)))