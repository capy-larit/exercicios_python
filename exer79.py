"""
Faça um programa em Python que receba do usuário sete números inteiros, calcule
e mostre:
a) Os números múltiplos de 2;
b) Os números múltiplos de 3;
"""

lista_2 = []
lista_3 = []

for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        lista_2.append(num)
    if num % 3 == 0:
        lista_3.append(num)
print(f'{lista_2} são múltiplos de 2.\n{lista_3} são múltuplos de 3.')
