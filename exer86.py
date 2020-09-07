"""
Crie um programa em Python que faça o controle de produtos da empresa XPTO.

- Exibir o seguinte menu:
1 - Cadastrar produto
2 - Alterar produto
3 - Excluir produto
4 - Listar estoque de peças
5 - Comprar produto
6 - Vender produto
7 - Sair

- Caso o usuário escolha a opção 1, o programa deve solicitar o código do
  produto, descrição do produto e quantidade do produto em estoque.
  Verificar se o código já existe no cadastro, pois não pode ter código
  duplicado. Depois retorna para o Menu.

- Caso o usuário escolha a opção 2, o programa deve solicitar a senha de acesso
  para alteração. Senha de acesso: yN1825*a

- Se o usuário digitar a senha correta, solicitar então o código do produto que
  será alterado. Se o código existir, mostrar a descrição e a quantidade em
  estoque cadastrados. O usuário pode alterar apenas a descrição e a quantidade
  em estoque. Se o código não existir, mostrar a seguinte mensagem na tela:
  “PRODUTO NÃO CADASTRADO.” Depois retorna para o Menu.

- Se o usuário digitar a senha incorreta, a mensagem de alerta ao usuário deve
  ser: “SENHA INCORRETA”. Depois retorna para o Menu.

IMPORTANTE: SE O USUÁRIO DIGITAR 3 VEZES A SENHA INCORRETA O PROGRAMA
            DEVE SER FINALIZADO APÓS MOSTRAR MENSAGEM: "SEU ACESSO FOI BLOQUEADO!
            PROCURE O ADMINISTRADOR"

- Caso o usuário escolha a opção 3, o programa deve solicitar a senha de acesso
  para alteração. Senha de acesso: yN1825*a

- Se o usuário digitar a senha correta, solicitar então o código do produto que
  será alterado. Se o código existir, mostrar a descrição, a quantidade em
  estoque e a mensagem: "DESEJA EXCLUIR O PRODUTO?" Se sim, excluir e mostrar
  na tela: "PRODUTO EXCLUIDO COM SUCESSO". Se não, apenas mostrar na tela.
  “PRODUTO NÃO EXCLUÍDO”. Se o código nãoexistir, mostrar a seguinte mensagem:
  “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu.

- Se o usuário digitar a senha incorreta, a mensagem de alerta ao usuário deve
  ser: “SENHA INCORRETA”. Depois retorna para o Menu.

IMPORTANTE: SE O USUÁRIO DIGITAR 3 VEZES A SENHA INCORRETA O PROGRAMA
            DEVE SER FINALIZADO APÓS EMITIR MENSAGEM: "SEU ACESSO FOI BLOQUEADO!
            PROCURE O ADMINISTRADOR"

- Caso o usuário escolha a opção 4, o programa deve mostrar na tela todos os
  produtos cadastrados e no final totalizar da seguinte maneira :
  *Ordem crescente de código do produto:

MODELO DE RELATÓRIO:
CÓDIGO       DESCRIÇÃO              QUANTIDADE EM ESTOQUE:
—————       —————————————              ———————————————-
1001       PASTA ESCOLAR TIPO 2        102
1002       PASTA ESCOLAR TIPO 1         97
1003       CANETA AZUL                 152

Total de produtos cadastrados: 3
Quantidade de itens em estoque: 351
Produtos com estoque abaixo do mínimo permitido (100 unidades): 1

- Caso o usuário escolha a opção 5, o programa deve solicitar o código do
  produto. Se o código existir no cadastro, mostrar na tela a descrição e a
  quantidade atual em estoque. Solicitar a quantidade de produtos que deseja
  comprar. A quantidade digitada pelo usuário deve somar com o estoque atual do
  produto em questão. Se o código não existir, mostrar a seguinte mensagem:
  “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu.

- Caso o usuário escolha a opção 6, o programa deve solicitar código do produto.
  Se o código existir no cadastro, mostrar na tela a descrição e a quantidade
  atual em estoque. Solicitar a quantidade de produtos que deseja vender.
  A quantidade digitada pelo usuário deve   subtrair com o estoque atual do
  produto em questão.

Importante: A quantidade em estoque não pode ficar negativa. Caso o usuário
            digite uma quantidade maior do que a que tem em estoque não
            permitir a venda.
            Se o código não existir, mostrar a seguinte mensagem:
            “PRODUTO NÃO CADASTRADO”. Depois retorna para o Menu.

- Caso o usuário escolha a opção 7, o programa deve ser finalizado.
——————————————————————————————————————————
- REGRAS:
a) Obrigatório o uso de laço de repetição
b) Obrigatório criar pelo menos 2 (duas) funções e fica a critério do aluno:
   com ou sem parâmetro e com ou sem return.

- Considerações:
a) Não há limite para cadastro de produtos
b) Se o usuário entrar com a senha correta (ao acessar a opção alterar ou
   excluir produto), não deve ser solicitada mais até o usuário sair do programa.
   O limite de tentativas para acesso, em caso de senha incorreta, é 3 tentativas.
c) Não permitir quantidade de produto menor ou igual a 0 (zero) mas opções 1, 2, 5 e 6.
d) O programa somente pode ser finalizado se o usuário escolher a opção 7 ou se
digitar 3 vezes a senha de acesso a opção 2 e 3 incorretamente.
"""

from sys import exit


def chamar_menu():
    return input(
        """-------------- Menu --------------
    1 - Cadastrar produto
    2 - Alterar produto
    3 - Excluir produto
    4 - Listar estoque de peças
    5 - Comprar produto
    6 - Vender produto
    7 - Sair
    Sua opção: """
    )


def cadastrar_produto(estoque):
    try:
        codigo = int(input('Digite o código do produto: '))
        if codigo in estoque:
            print('Código de produto já existente.')
        else:
            descricao = input('Digite a descrição do produto: ')
            quantidade = int(input('Digite a quantidade: '))
            if quantidade <= 0:
                print(
                    'NÃO É POSSÍVEL CADASTRAR UMA QUANTIDADE IGUAL OU MENOR QUE ZERO'
                )
            else:
                estoque[codigo] = [descricao, quantidade]
    except ValueError:
        print('DEVE SER UM NÚMERO')
    finally:
        return estoque


def alterar_produto(estoque, cont):
    senha = input('Digite a SENHA: ')
    # criar um função
    if senha != 'yN1825*a':
        cont += 1
        print('SENHA INCORRETA')
    if senha != 'yN1825*a' and cont == 3:
        print('SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR')
        exit()
    if senha == 'yN1825*a':
        try:
            codigo = int(
                input('Digite o código do produto que deseja alterar: ')
            )
            if codigo in estoque:
                print(
                    f'DESCRIÇÃO: {estoque.get(codigo)[0]}\nQUANTIDADE: {estoque.get(codigo)[1]}'
                )
                descricao = input('Digite a nova descrição: ')
                qtd_nova = int(input('Digite a nova quantidade em estoque: '))
                if qtd_nova <= 0:
                    print(
                        'O ESTOQUE NÃO ACEITA QUANTIDADES NEGATIVAS OU IGUAIS A ZERO'
                    )
                else:
                    estoque[codigo] = [descricao, qtd_nova]
            else:
                print('PRODUTO NÃO CADASTRADO')
        except ValueError:
            print('DEVE SER UM NÚMERO')
    return estoque, cont


def excluir_produto(estoque, cont_excluir):
    try:
        senha = input('Digite a SENHA: ')
        if senha != 'yN1825*a':
            cont_excluir += 1
            print('SENHA INCORRETA')
        if senha != 'yN1825*a' and cont_excluir == 3:
            print('SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR')
            exit()
        if senha == 'yN1825*a':
                codigo = int(input('Digite o código do produto que deseja alterar: '))
                if codigo in estoque:
                    print(
                        f'DESCRIÇÃO: {estoque.get(codigo)[0]}\nQUANTIDADE: {estoque.get(codigo)[1]}'
                    )
                    sim_nao = input('\nDESEJA EXCLUIR O PRODUTO? ').upper()
                    if sim_nao == 'SIM':
                        del estoque[codigo]
                        print('PRODUTO EXCLUÍDO COM SUCESSO')
                    elif sim_nao == 'NAO':
                        print('PRODUTO NÃO EXCLUÍDO')
                else:
                    print('PRODUTO NÃO CADASTRADO')
        return estoque, cont_excluir
    except ValueError:
        print('DEVE SER UM NÚMERO')
        return estoque, cont


def listar_estoque(estoque):
    ordenada = list(estoque.keys())
    ordenada.sort()
    print('CÓDIGO           DESCRIÇÃO                  QUANTIDADE EM ESTOQUE ')
    print('--------------   ----------------------     ------------------------')
    soma = qts_abaixo = 0
    for key in ordenada:
        print(f'{key: <16} {estoque[key][0]: <20} {estoque[key][1]: >10}')
        soma += estoque[key][1]
        if estoque[key][1] < 100:
            qts_abaixo += 1
    print(f'Total de produtos cadastrados: {len(estoque)}')
    print(f'Quantidade de itens em estoque: {soma}')
    print(
        f'Produtos com estoque abaixo do mínimo permitido (100 unidade): {qts_abaixo}'
    )
    return estoque


def comprar_produto(estoque):
    try:
        codigo = int(input('Digite o código do produto que deseja comprar: '))
        if codigo in estoque:
            print(
                f'DESCRIÇÃO: {estoque.get(codigo)[0]}\nQUANTIDADE: {estoque.get(codigo)[1]}'
            )
            qtd_comprar = int(input('Digite a quantidade que deseja comprar: '))
            if qtd_comprar <= 0:
                print(
                    'O ESTOQUE NÃO ACEITA QUANTIDADES NEGATIVAS OU IGUAIS A ZERO'
                )
            else:
                estoque[codigo] = [
                    estoque.get(codigo)[0],
                    estoque.get(codigo)[1] + qtd_comprar,
                ]
        else:
            print('PRODUTO NÃO CADASTRADO')
        return estoque
    except ValueError:
        print('DEVE SER UM NÚMERO')
        return estoque


def vender_produto(estoque):
    try:
        codigo = int(input('Digite o código do produto que deseja vender: '))
        if codigo in estoque:
            print(
                f'DESCRIÇÃO: {estoque.get(codigo)[0]},\nQUANTIDADE: {estoque.get(codigo)[1]}'
            )
            qtd_vender = int(input('Digite a quantidade que deseja vender: '))
            if qtd_vender <= 0 or qtd_vender > estoque.get(codigo)[1]:
                print(
                    'QUANTIDADE ACIMA DO LIMITE DE ESTOQUE OU IGUAL A ZERO OU NEGATIVA'
                )
            else:
                estoque[codigo] = [
                    estoque.get(codigo)[0],
                    estoque.get(codigo)[1] - qtd_vender,
                ]
        else:
            print('PRODUTO NÃO CADASTRADO')
        return estoque
    except ValueError:
        print('DEVE SER UM NÚMERO')
        return estoque


def sair():
    print('SAINDOOOOOO')
    exit()


estoque = {}
gerenciar_fluxo = {
    '1': cadastrar_produto,
    '2': alterar_produto,
    '3': excluir_produto,
    '4': listar_estoque,
    '5': comprar_produto,
    '6': vender_produto,
    '7': sair,
}
opcao = cont = cont_excluir = 0
while True:
    opcao = chamar_menu()
    if opcao == '2':
        estoque, cont = gerenciar_fluxo[opcao](estoque, cont)
    elif opcao == '3':
        estoque, cont_excluir = gerenciar_fluxo[opcao](estoque, cont_excluir)
    elif opcao == '7':
        gerenciar_fluxo[opcao]()
    else:
        estoque = gerenciar_fluxo[opcao](estoque)
