'''
Faça um programa em Python que solicite ao usuário um número inteiro e
mostre na tela os próximos 10 números inteiros a partir do número digitado.
'''

num = int(input('Digite um número inteiro: '))
limite = num + 10

print('Os próximos dez números são: ')

while num < limite:
  print(num)
  num += 1
