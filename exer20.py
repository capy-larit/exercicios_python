'''
Faça um algoritmo que calcule a raiz do número recebido.
'''

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
