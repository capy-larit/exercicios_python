"""
Faça um programa em Python que seja capaz de obter o resultado de uma
exponenciação para qualquer base e expoente inteiro fornecido.
"""

base = int(input("Digite um número inteiro para a base: "))
exp = int(input("Digite um número inteiro para o expoente: "))
cont = 0
while cont < 1:
    cal = base ** exp
    print("A potencia é {}.".format(cal))
    cont += 1
