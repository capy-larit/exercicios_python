"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
já são maiores.
"""

contagemMaior = 0
contagemMenor = 0

for cont in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(cont)))
    idade = 2020 - ano
    if idade >= 21:
        contagemMaior += 1
    else:
        contagemMenor += 1
print(
'{} pessoas ainda não atingiram a maioridade.'.format(contagemMenor)
)

print('{} pessoas já são maiores.'.format(contagemMenor))
