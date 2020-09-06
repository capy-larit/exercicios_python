"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.
"""

resp = 'S'
cont = soma = maiorNum = menorNum =0
# [0] para pegar só a primeira letra
while resp in 'S':
    num = int(input('Digite um número: '))
    resp = input('Deseja continua? [S/N] ').upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maiorNum = menorNum = num
    else:
        if num < menorNum:
            menorNum = num
        elif num > maiorNum:
            maiorNum = num

print(f'Você digitou {cont} números e a média foi {soma/cont}\nO maior valor foi {maiorNum} e o menor foi {menorNum}.')
