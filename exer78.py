"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
- Quantas pessoas tem mais de 18 anos;
- Quantos homens foram cadastrados;
- Quantas mulheres tem menos de 20 anos.
"""

cont18 = contMasc = contMu =  0
while True:
    print(50 * '=')
    print('                CADASTRE UMA PESSOA           ')
    print(50 * '=')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').upper()
    print(50 * '=')
    resp = input('Deseja continuar? [S/N]: ').upper()
    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N]: ').upper()
    if 'N' in resp:
        break
    else:
        if idade > 18:
            cont18 += 1
        if sexo == 'M':
            contMasc += 1
        if sexo == 'F' and idade < 20:
            contMu += 1
print(f'Total de pessoas com mais de 18 anos: {cont18}\nAo todo temos {contMasc} homens cadastrados\nE temos {contMu} mulheres com menos de 20 anos.')
