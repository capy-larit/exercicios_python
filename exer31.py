'''
Faça um programa em Python que receba do usuário três números inteiros e mostre-os na tela em ordem crescente. 

>>> Caso o usuário digite três números iguais, mostrar na tela a informação: OS TRÊS NÚMEROS DIGITADOS SÃO IGUAIS.
'''

numero = int(input('Digite o primeiro número: '))
numero_1 = int(input('Digite o segundo número: '))
numero_2 = int(input('Digite o terceiro número: '))

if numero == numero_1 and numero == numero_2:
  print('Os três números digitados são iguais.')

else:
 lista = [numero, numero_1, numero_2]
 lista.sort ()

 print('A ordem crescente é {}'.format((lista)))