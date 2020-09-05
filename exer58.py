"""
10) Escreva um algoritmo que solicite n idades. Mostrar na tela:
A) Quantas pessoas possuem 18 anos
B) Quantas pessoas possuem mais de 18 anos
C) Quantas pessoas possuem menos de 18 anos
D) Soma das idades digitadas
E) Média das idades digitadas
F) Maior idade e quantas pessoas possuem essa idade
G) Menor idade e quantas pessoas possuem essa idade
Observação: n é um número também fornecido pelo usuário. Por exemplo, se o
usuário digitar 15 para n, você terá que solicitar 15 idades.
"""

num = int(input('Digite a quantidade de idades: '))
cont = 0
cont18 = 0
contMais18 = 0
contMenos18 = 0
soma = 0
contMaiorIdade = 0
contMenorIdade = 0
maior_idade = 0
menor_idade = 0

while cont < num:
    idade = int(input('Digite uma/outra idade: '))
    soma += idade
    if idade == 18:
        cont18 +=1
    if idade > 18:
        contMais18 += 1
    if idade < 18:
        contMenos18 += 1
    if cont == 0:
        maior_idade = idade
        contMaiorIdade += 1
        contMaiorIdade = 0

        menor_idade = idade
        contMenorIdade += 1
        contMenorIdade = 0
    else:
        if idade >= maior_idade:
            maior_idade = idade
            contMaiorIdade += 1


        if idade <= menor_idade:
            menor_idade = idade
            contMenorIdade += 1

    cont += 1
print('{} pessoas possuem 18 anos.'.format(cont18))
print('{} pessoa possuem mais de 18 anos.'.format(contMais18))
print('{} pessoa possuem menos de 18 anos.'.format(contMenos18))
print('Soma das idades digitadas {}.'.format(soma))
print('A média das idades digitadas é {}.'.format(soma/num))
print('A maior idade digitada foi {} e {} pessoas possuem essa idade.'.format(maior_idade, contMaiorIdade))
print('A menor idade digitada foi {} e {} pessoas possuem essa idade.'.format(menor_idade, contMenorIdade))
