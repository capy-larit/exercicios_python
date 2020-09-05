"""
Mostre a tabuada de um número que o usuário escolher.
"""

tab = int(input('Qual tabuada deseja saber: '))

for cont in range(1, 11):
    print('{} x {} = {}'. format(tab, cont, tab * cont))
print('FIM')
