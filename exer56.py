"""
Imagine uma brincadeira entre dois colegas, na qual um pensa um número e
o outro deve fazer chutes até acertar o número imaginado. Como dica, a cada
tentativa é dito se o chute foi alto ou baixo. Elabore um algoritmo em Python
dentro deste contexto, que leia o número digitado pelo usuário e os chutes,
ao final mostre quantas tentativas foram necessárias para descobrir o
número.
Exemplo:
Número: 85
Chute número 1: 50
*** CHUTOU BAIXO ***
Chute número 2: 62
*** CHUTOU BAIXO ***
Chute número 3: 89
*** CHUTOU ALTO ***
Chute número 4: 80
*** CHUTOU BAIXO ***
Chute número 5: 85
*** ACERTOU! PARABÉNS! VOCÊ PRECISOU DE 5 CHANCES ***
"""

num = int(input('Digite o número: '))
chute = int(input('Digite o seu chute: '))
qtdChute = 1

while True:
    if chute < num:
        print('Chute número {}: {}\nVocê chutou baixo.'.format(qtdChute,chute))
        qtdChute += 1
        chute = int(input('Digite o seu chute: '))
    elif chute > num:
        print('Chute número {}: {}\nVocê chutou alto.'.format(qtdChute, chute))
        qtdChute += 1
        chute = int(input('Digite o seu chute: '))
    elif chute == num:
        print('Chute número {}: {}\nACERTOU! parabéns! Você precisou de {} chances'.format(qtdChute, chute, qtdChute))
        exit()
