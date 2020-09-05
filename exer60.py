"""
Faça um algoritmo em Python que receba do usuário um número inteiro
(maior que 0) e mostre na tela a tabuada do número digitado. Após mostrar a
tabuada, o programa deve perguntar se o usuário quer continuar ou encerrar.
O programa deve mostrar quantas tabuadas o usuário desejar.
"""

cont = 1
continua = 1
num = 0

while continua == 1:
    print(50 * '=')
    num = int(input('Qual tabuada deseja saber: '))
    print(50 * '=')

    while cont <= 10 and continua == 1:
        print('{} x {} = {}'.format(num,cont, num * cont))
        cont += 1

    print(50 * '=')
    continua = int(input('Deseja continuar?\n Sim = 1\n Não = 0\n'))
    print(50 * '=')
    cont -= 10
