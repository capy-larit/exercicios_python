'''
Faça um programa em Python que solicitei ao usuário dois números inteiros e
mostre na tela a soma dos elementos existentes entre os dois números
informados.
'''

numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input(
  'Digite outro número inteiro: ')
  )

soma = 0

if numero_1 < numero_2:
  numero_1 += 1
  while numero_1 < numero_2:
    soma = soma + numero_1
    numero_1 += 1
  print(soma)

elif numero_2 < numero_1:
  numero_2 += 1
  while numero_2 < numero_1:
    soma = soma + numero_2
    numero_2 += 1
  print(soma)

else:
  print('Digite números distintos.')
