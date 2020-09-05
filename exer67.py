"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

s = 0

for cont in range(0, 6):
    num = int(input('Digite um/outro número: '))
    if num % 2 == 0:
        s += num

print('A soma dos números pares digitados é {}.'.format(s))
