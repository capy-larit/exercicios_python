"""
Escreva um algoritmo em Python que leia 20 números inteiros e mostre qual
foi o maior e o menor valor fornecido.
"""

limite = 5
cont = 0

while cont < 5:
    num = int(input('Digite um número: '))
    if cont == 0:
        maiorNum = num
        menorNum = num
    else:
        if num > maiorNum:
            maiorNum = num
        if num < menorNum:
            menorNum = num
    cont += 1
print('O maior número digitado foi {}.\nO menor número digitado foi {}.'.format(maiorNum, menorNum))
