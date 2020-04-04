'''
Faça um programa em Python que solicite ao usuário um número inteiro e retorne se é par ou ímpar.
'''

numero = int(input('Digite um número inteiro: '))

resultado = numero % 2

if resultado == 0:
  print('O número digitado é par.')

else:
  print('O número digitado é ímpar.')