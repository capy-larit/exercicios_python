'''
Faça um programa em Python que solicite ao usuário um número inteiro e retorne se é múltiplo de 5 e de 10 ao mesmo tempo.
'''

numero = int(input('Digite um número inteiro: '))

resultado = numero % 5
resultado_1 = numero % 10

if resultado == 0 and resultado_1 == 0:
  print('Esse número é múltiplo de 5 e de 10.')

else:
  print('Esse número não é múltiplo de 5 e de 10.')