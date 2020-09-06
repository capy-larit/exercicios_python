"""
Crie um algoritmo em que o computador sorteie um número e o usuário tente
acertar qual é esse número. No final diga em quantas tentativas ele acertou.
"""

# Sorteia um número
from random import randint
computador = randint(0, 10)

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi? ')
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas.'.format(cont))
