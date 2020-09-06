"""
Uma escola deseja saber se existem alunos cursando, simultaneamente, as
disciplinas Computacional Thinking using Python e Domain Driven Design.
Coloque os números das matrículas dos alunos que cursam Computacional Thinking
using Python em uma lista.
Coloque os números das matrículas dos alunos que cursam Domain Driven Design
em outra lista. Mostre o número das matrículas que aparecem nas duas listas.
Importante:
Não sabemos quantos alunos estão cursando as disciplinas. Encontre uma solução
para que o usuário digite as matrículas e quando quiser consiga terminar o
programa.
"""

lista_CTP = []
lista_DDD = []
lista_iguais = []

while True:
    print(100 * '=')
    opcao = input('Qual disciplica CTP (Computacional Thinking using Python) ou DDD (Domain Driven Design)?\nDigite 0 para sair.\nSua opção: ').strip().upper()
    if opcao != 'CTP' and opcao != 'DDD' and opcao != '0':
        print(100 * '=')
        opcao = input('Opção Inválida! Qual disciplica CTP ou DDD?\nDigite 0 para sair.\nSua opção: ').strip().upper()
    elif opcao == 'CTP':
        print(100 * '=')
        lista_CTP.append(int(input('Número de matrícula: ')))
    elif opcao == 'DDD':
        print(100 * '=')
        lista_DDD.append(int(input('Número de matrícula: ')))
    elif opcao == '0':
        print(100 * '=')
        print('Saindo...')
        break
if lista_CTP > lista_DDD:
    for i in range(len(lista_CTP)):
        for item in range(len(lista_DDD)):
            if lista_CTP[i] == lista_DDD[item]:
                lista_iguais.append(lista_CTP[i])
else:
    for i in range(len(lista_DDD)):
        if lista_DDD[i] == lista_CTP:
            lista_iguais.append(lista_DDD[i])
for rm in lista_CTP:
    if rm in lista_DDD:
        lista_iguais.append(rm)
print(f'Alunos cursando as duas materias: {lista_iguais}')
print(f'Alunos cursando a matéria de CTP: {lista_CTP}')
print(f'Alunos cursando a matéria de DDD: {lista_DDD}')
