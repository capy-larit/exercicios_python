"""
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 50.
"""

s = 0
for cont in range(1, 500, 2):
    if cont % 3 == 0:
        s += cont
print('A soma dos números ímpares e múltiplos de 3 entre 1 até 50 é {}.'.format(s))
print('FIM')
