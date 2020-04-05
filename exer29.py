'''
Faça um programa em Python que receba dois números inteiros e mostre na tela o maior número digitado.
'''


numero = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if numero > numero_2:
  print('O maior número digitado foi {}.'.format(numero))

elif numero_2 > numero:
  print('O maior número digitado foi {}.'.format(numero_2))