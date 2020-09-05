"""
Faça um programa em Python que efetue a soma de todos os números
ímpares que são múltiplos de 3 e que se encontram no conjunto dos números
de 1 até 500.
"""

limite = 500
soma = 0

cont = 3
while cont < limite:
    if cont % 2 != 0 and cont % 3 == 0:
        soma += cont
    cont += 1
print('A soma é {}.'.format(soma))
