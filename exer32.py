'''
Escreva um programa em Python que solicite ao usuário 3 (três) números inteiros e retorne se os números foram ou não foram digitados em ordem crescente.
'''

numero = int(input('Digite o primeiro número: '))
numero_1 = int(input('Digite o segundo número: '))
numero_2 = int(input('Digite o terceiro número: '))

if numero < numero_1 and numero < numero_2 and numero_1 < numero_2:
  print('Os números foram digitados em ordem crescente.')

elif numero_1 < numero or numero_1 > numero_2:
  print('Os números não foram digitados em ordem crescente.')

elif numero_2 < numero or numero_2 < numero_1:
  print('Os números não foram digitados em ordem crescente.')