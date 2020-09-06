"""
Faça um programa que leia um número qualquer e mostre o seu factorial.
"""
# OUTRA FORMA DE FAZER
# from math import factorial
# n = int(input('Digite um número para calcular seu factorial: '))
# f = factorial(n)
# print('O factorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu factorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1

print('{}.'.format(f))
