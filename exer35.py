'''
Escreva um programa em Python que receba dois números reais. Verifique se a soma dos números digitados é maior que 10 e mostre na tela: Se a soma for maior que 10, mostrar na tela: Número maior que 10. Se a soma for menor ou igual a 10, mostrar na tela: Número menor ou igual a 10
'''

numero = float(input('Digite um número: '))
numero_1 = float(input('Digite outro número: '))

soma = numero + numero_1

if soma > 10:
  print('Número maior que 10.')

else:
  print('Número menor ou igual a 10.')