"""
Escreva um algoritmo em Python que receba a quantidade de alunos de
uma turma e solicite o nome e a nota de cada aluno.
No final informe qual aluno obteve a maior nota.
"""

print(50 * '=')
qtd = int(input('Quantos alunos a turma tem? '))
print(50 * '=')
cont = 0
maior = 0

while cont < qtd:
    cont += 1
    print('Aluno ',cont)
    nome = input('Nome do aluno: ')
    nota = float(input('Nota de {}: '.format(nome)))
    print(50 * '=')
    if nota > maior:
        maior = nota
        nome_maior = nome

print('A maior nota foi {} de {}.'.format(maior, nome_maior))
