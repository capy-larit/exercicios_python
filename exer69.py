"""
Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo.
"""

contPrimo = 0

num = int(input('Digite um número: '))
for cont in range(1, num + 1):
    if num % cont == 0:
        contPrimo += 1

if contPrimo == 2:
    print('O número digitado é um número primo')

else:
    print('Não é um número primo.')
