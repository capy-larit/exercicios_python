'''
Faça um programa em Python que mostre o menu de opções a seguir: 
Menu de Opções 
1. Somar dois números 
2. Raiz quadrada de um número 
Digite a opção desejada: 

Receba a opção do usuário e os dados necessários para executar cada operação.
'''

import math

menu = int(input(
  'Menu de Opções:\n1.Somar dois números;\n2.Raiz quadrada de um número;\nDigite a opção desejada: ')
)

if menu == 2:
  numero_raiz = int(input('Digite o número: '))
  if numero_raiz <= -1:
    print('Não existe raiz de número negativo.')
  else:
   print('A raiz de {} é {}'.format(numero_raiz, math.sqrt(numero_raiz)))


elif menu == 1:
  numero = int(input('Digite o primeiro número: '))
  numero_1 = int(input('Digite o segundo número: '))
  print(
    '{} + {} = {}'.format(numero, numero_1, numero + numero_1)
  )
