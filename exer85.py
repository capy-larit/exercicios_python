"""
Utilizando listas faça um programa que faça 5 perguntas para um pessoa sobre
um crime

as perguntas são:
a) Telefonou para a vítima?
b) Esteve no local do crime?
c) Mora perto da vítima?
d) Devia para a vítima?
e) Já trabalhou para a vítima?

O programa em Python deve no final emitir uma classificação sobre a participação
 da pessoa no crime. Se a pessoa responder positivamente a:
2 questões ela deve ser classificada como SUSPEITA.
3 ou 4 questões como CÚMPLICE.
5 questões como ASSASINO.
Caso contrário, ele será classificado como INOCENTE.

Importante: Usar pelo menos uma função.
"""

def simOuNao(resposta):
        return(print('Responda com SIM ou NAO'))

lista = []
resposta = input('Telefonou para a vítima? ').upper()
while resposta != 'SIM' and resposta != 'NAO':
    simOuNao(resposta)
    resposta = input('Telefonou para a vítima? ').upper()
lista.append(resposta)
resposta = input('Esteve no local do crime? ').upper()
while resposta != 'SIM' and resposta != 'NAO':
    simOuNao(resposta)
    resposta = input('Esteve no local do crime? ').upper()
lista.append(resposta)
resposta = input('Mora perto da vítima? ').upper()
while resposta != 'SIM' and resposta != 'NAO':
    simOuNao(resposta)
    resposta = input('Mora perto da vítima? ').upper()
lista.append(resposta)
resposta = input('Devia para a vítima? ').upper()
while resposta != 'SIM' and resposta != 'NAO':
    simOuNao(resposta)
    resposta = input('Devia para a vítima? ').upper()
lista.append(resposta)
resposta = input('Já trabalhou para a vítima? ').upper()
while resposta != 'SIM' and resposta != 'NAO':
    simOuNao(resposta)
    resposta = input('Já trabalhou para a vítima? ').upper()
lista.append(resposta)
if all(i == 'SIM' for i in lista):
    print('Classificação: ASSSASINO')
else:
    print(lista.count('SIM'))
    if lista.count('SIM') == 2:
        print('Classificação: SUSPEITA')
    elif lista.count('SIM') == 3 or lista.count('SIM') == 4:
        print('Classificação: CÚMPLICE')
    else:
        print('Classificação: INOCENTE')
