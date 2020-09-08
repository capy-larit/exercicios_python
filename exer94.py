"""
Faça um programa em Python que leia 4 notas, mostre as notas e a média na tela.
"""

lista = []
soma = 0
for i in range(4):
    try:
        nota = float(input(f'Digite a {i + 1}ª nota: '))
        lista.append(nota)
        soma += nota
    except ValueError:
        print('A nota deve ser um número.')
        nota = float(input(f'Digite a {i + 1}ª nota: '))
        lista.append(nota)
        soma += nota

media = soma / 4
print('-' * 30)
for i in lista:
    print(f'Nota: {i}')
print(f'Média: {media}')
