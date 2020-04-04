'''
Faça um algoritmo em Python para ler dois números inteiros (num1 e num2) e informar se num1 é divisível por num2
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

conta = num1 % num2
if conta != 0:
  print(
    'O primeiro número digitado não é divisível pelo segundo número.'
  )

else:
  print('O primeiro número digitado é divisível pelo segundo número.\nE o resultado é {}'.format(num1/num2))