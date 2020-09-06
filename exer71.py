"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.

No final do programa mostre:
- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos.
"""

hMaisVelho = 0
contagem = 0
contIdade = -1

for cont in range(0, 5):
    print(50 * '=')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [F/M]: ').upper()
    print(50 * '=')
    contIdade += idade
    if sexo == 'M' and idade > hMaisVelho:
        hMaisVelho = idade
        nomeMaisVelho = nome
    elif sexo == 'F' and idade < 20:
        contagem += 1

print('A média das idades é {}.'.format(contIdade / 4))
print('O homem mais velho é {}.'.format(nomeMaisVelho))
print('{} mulheres têm menos de 20 anos.'.format(contagem))
