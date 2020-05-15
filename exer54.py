'''
Faça um programa em Python que mostre na tela as tabuadas do 1, 2, 3, 4,
5, 6, 7, 8, 9 e 10.
Observação:
- Utilizar um ou dois laços de repetição para
  realização desse exercício.
'''

tab = 1
multiplicador = 1

while tab <= 10:
    while multiplicador <= 10:
        print('{} x {} = {}'.format(tab, multiplicador, tab * multiplicador))
        multiplicador += 1
    multiplicador = 1
    tab += 1
