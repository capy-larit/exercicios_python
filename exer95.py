"""
Faça um programa utilizando um dict (dicionário) que leia dados de entrada do usuário. O
usuário deve entrar com os dados de uma pessoa como nome, idade e cidade onde mora.
Após isso, você deve imprimir os dados como o exemplo abaixo:
nome: João
idade: 20
cidade: São Paulo
"""

def chamar_menu():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite sua cidade: ')
    dict[nome]=[idade, cidade]

dict = {}
try:
    chamar_menu()
except:
    print('A idade deve ser um número inteiro.')
    chamar_menu()

for chave, item in dict.items():
    print(f'Nome: {chave}\nIdade: {item[0]}\nCidade: {item[1]}')
