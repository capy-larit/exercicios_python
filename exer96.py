"""
Utilize o exercício anterior e altere de modo que o usuário possa adicionar quantas pessoas
desejar. Quando o usuário quiser finalizar a inclusão, mostrar na tela um relatório com os
dados de cada pessoa.
"""

def chamar_menu():
    chave = input('Digite seu nome: ')
    dic[chave] = int(input('Digite sua idade: ')), input('Digite sua cidade: ')
    sair = input('Digite 0 para sair: ')
    if sair == '0':
        for chave, item in dic.items():
            print('=' * 30)
            print(f'Nome: {chave}\nIdade: {item[0]}\nCidade: {item[1]}')
        exit()


dic = {}
sair = 1
while True:
    chamar_menu()
