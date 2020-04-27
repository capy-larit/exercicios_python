'''
Elabore um programa em Python que seja capaz de contar a quantidade de
números ímpares existentes entre dois números fornecidos pelo usuário.
'''

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite um número maior: '))

cont = 0

if numero_1 > numero_2 or numero_1 == numero_2:
  print(
  f'''\nEste error pode ter ocorrido:
  1. Ou primeiro número digitado é maior que o segundo.
  2. Ou os números digitados sãão iguais.'''
  )

elif numero_1 % 2 != 0:
  while numero_1 < numero_2 and numero_1 != numero_2 - 1 and numero_1 != numero_2 - 2:
    numero_1 = numero_1 + 2
    cont += 1
    print(numero_1)

elif numero_1 % 2 == 0:
  numero_1 += 1
  print(numero_1)
  while numero_1 < numero_2 and numero_1 != numero_2 - 1 and numero_1 != numero_2 - 2:
    numero_1 = numero_1 + 2
    cont += 1
    print(numero_1)
