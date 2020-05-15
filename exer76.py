'''
Faça um programa  que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso digitado.
'''

pesoMaior = 0
pesoMenor = 0

for cont in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(cont)))
    if cont == 1:
        pesoMaior = peso
        pesoMenor = peso

    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print('O menor peso foi {} Kg.\nO maior peso foi {} Kg.'.format(pesoMenor, pesoMaior))
