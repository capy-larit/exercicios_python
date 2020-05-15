'''
A empresa FOGUETE possui um ônibus com 48 lugares (24 nas janelas e 24 no
corredor). Escreva um programa em Python que utilize 2 listas para controlar as
poltronas que serão ocupadas no corredor e na janela.

Considerações:
- 0 significa poltrona desocupada
- 1 significa poltrona ocupada
- O programa inicia com todas as poltronas desocupadas.

- Janela (Lista1)
    0 0 0 0 0 0      0  0  0
    0 1 2 3 4 5 ... 21 22 23
- Corredor (Lista2)
    0 0 0 0 0 0      0  0  0
    0 1 2 3 4 5 ... 21 22 23

-A seguir mostrar o seguinte menu:
    1 - Vender passagem
    2 - Cancelar compra
    3 - Mostrar mapa de ocupação
    4 - Sair

- Quando a opção escolhida for 1 (Vender passagem), deverá ser
  perguntado se o usuário deseja janela ou corredor e o número da poltrona (de 1 a
  24). O programa deverá verificar se está livre, ou seja, se o conteúdo no índice
  (número da poltrona desejada – 1) está preenchido com 0. O programa deverá,
  então, dar uma das seguintes mensagens:
    - Venda realizada com sucesso! – Se a poltrona solicitada estiver livre, marcando-a
      como ocupada.
    - Poltrona ocupada. Venda não realizada! – Se a poltrona solicitada não estiver
      disponível para venda.

- Quando a opção escolhida for 2 (Cancelar passagem), o
  programa deverá perguntar qual o número da poltrona (de 1 a 24), se é janela ou
  corredor que deseja cancelar a compra. Se a poltrona estiver realmente ocupada
  (preenchido com 1) deverá trocar para 0 (desocupada). Emitir uma das seguintes
  mensagens:
      - Compra cancelada com sucesso! - Se a poltrona solicitada estiver ocupada,
      marcando-a como livre.
      - Poltrona livre. Compra não cancelada! - Se a poltrona solicitada não estiver
      ocupada.

- Quando o usuário escolher a opção 3 (Mostrar mapa de
  ocupação), mostrar na tela o exemplo de listagem abaixo:
      Janela            Corredor
      1- Ocupada      1- Ocupada
      2- Ocupada      2- Livre
      3- Livre        3- Livre
      4- Livre        4- Livre
      5- Ocupada      5- Ocupada
      ...             ...
- Quando a opção 4 for escolhida (Sair), a execução do programa
  deverá ser finalizada.

 -Validações:
    - Não aceitar opção diferente de 1, 2, 3 e 4.
    - Não permitir acesso ao 1 - Vender passagem quando todas as
      poltronas já estiverem ocupadas. Nesse caso, emitir a seguinte mensagem:
      Ônibus lotado. Opção inválida!
    - Não permitir acesso ao 2 - Cancelar compra se não tiver poltrona
      ocupada. Nesse caso, emitir a seguinte mensagem:
      Todas as poltronas estão livres. Opção inválida!
'''
lista_ocupado_janela = []
lista_ocupado_corredor = []
lista_lugares_janela = []
lista_lugares_corredor = []

print(22 * '=','MENU',22 * '=')
opcao = (input('1- Vender passagem.\n2- Cancelar compra.\n3- Mostrar mapa de ocupação.\n4- Sair.\nSua opção: ')).strip()
print(50 * '=')

for livre in range(24):
    lista_lugares_janela.append("- Livre")
    lista_lugares_corredor.append("- Livre")
    lista_ocupado_janela.append(0)
    lista_ocupado_corredor.append(0)

while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
    opcao = input("Opção inválida! Digite apenas 1, 2, 3 ou 4: ").strip()

while opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
    if opcao == '1' and all(i == 1 for i in lista_ocupado_janela) and all(i == 1 for i in lista_ocupado_corredor):
        print('Ônibus lotado. Opção inválida!')
    elif opcao == '1':
        lugar = input('Deseja uma poltrona na janela ou no corretor?\nJ- Janela\nC- Corredor\nSua opção: ').upper().strip()
        while lugar != 'J' and lugar != 'C':
            print(50 * '=')
            lugar = input('Opção Inválida!\nDigite J ou C.\nSua opção: ').upper().strip()
            print(50 * '=')
        if lugar == 'J':
            print(50 * '=')
            num = int(input('Qual o número da poltrona que deseja? Entre 1 a 24.\nSua opção: '))
            while num > 24 or num < 1:
                print(50 * '=')
                num = int(input('Opção inválida. As poltronas são de 1 a 24.\nSua opção: '))
            if lista_ocupado_janela[num - 1] == 1:
                print('Poltrona ocupada. Venda não realizada!')
            else:
                del lista_ocupado_janela[num - 1]
                lista_ocupado_janela.insert(num - 1, 1)
                del lista_lugares_janela[num - 1]
                lista_lugares_janela.insert(num - 1, '- Ocupado')
                print('Venda realizada com sucesso!')
            print(50 * '=')

        if lugar == 'C':
            print(50 * '=')
            num = int(input('Qual o número da poltrona que deseja? Entre 1 a 24.\nSua opção: '))
            while num > 24 or num < 1:
                print(50 * '=')
                num = int(input('Opção inválida. As poltronas são de 1 a 24.\nSua opção: '))
            if lista_ocupado_corredor[num - 1] == 1:
                print('Poltrona ocupada. Venda não realizada!')
            else:
                del lista_ocupado_corredor[num - 1]
                lista_ocupado_corredor.insert(num - 1, 1)
                del lista_lugares_corredor[num - 1]
                lista_lugares_corredor.insert(num - 1, '- Ocupado')
                print('Venda realizada com sucesso!')

    if opcao == '2' and all(i == 0 for i in lista_ocupado_janela) and all(i == 0 for i in lista_ocupado_corredor):
        print('Todas as poltronas estão livres. Opção inválida!')
    elif opcao == '2':
        lugar = input('Deseja cancelar uma passagem com assento na janela ou no corretor?\nJ- Janela\nC- Corredor\nSua opção: ').upper().strip()
        while lugar != 'J' and lugar != 'C':
            print(50 * '=')
            lugar = input('Opção Inválida!\nDigite J ou C.\nSua opção: ').upper().strip()
            print(50 * '=')
        if lugar == 'J':
            print(50 * '=')
            num = int(input('Qual o número da poltrona que deseja cancelar? Entre 1 a 24.\nSua opção: '))
            while num > 24 or num < 1:
                print(50 * '=')
                num = int(input('Opção inválida. As poltronas são de 1 a 24.\nSua opção: '))
            if lista_ocupado_janela[num - 1] == 0:
                print(lista_ocupado_janela[num - 1])
                print(50 * '=')
                print('Poltrona livre. Compra não cancelada!')
            else:
                del lista_ocupado_janela[num - 1]
                lista_ocupado_janela.insert(num - 1, 0)
                del lista_lugares_janela[num - 1]
                lista_lugares_janela.insert(num - 1, '- Livre')
                print('Compra cancelada com sucesso!')
            print(50 * '=')

        if lugar == 'C':
            print(50 * '=')
            num = int(input('Qual o número da poltrona que deseja cancelar? Entre 1 a 24.\nSua opção: '))
            while num > 24 or num < 1:
                print(50 * '=')
                num = int(input('Opção inválida. As poltronas são de 1 a 24.\nSua opção: '))
            if lista_ocupado_corredor[num - 1] == 0:
                print(50 * '=')
                print('Poltrona livre. Compra não cancelada!')
            else:
                del lista_ocupado_corredor[num - 1]
                lista_ocupado_corredor.insert(num - 1, 0)
                del lista_lugares_corredor[num - 1]
                lista_lugares_corredor.insert(num - 1, '- Livre')
                print('Compra cancelada com sucesso!')

    if opcao == '3':
        print(50 * '=')
        print('\t','Janela','\t','\t','Corredor\n')
        for lista in range(1, 25):
            print('\t',lista, lista_lugares_janela[lista - 1], '\t','\t',lista, lista_lugares_corredor[lista - 1])

    if opcao == '4':
        print('Obrigada por comprar conosco! Até a próxima.')
        break

    print(22 * '=','MENU',22 * '=')
    opcao = (input('Deseja fazer mais alguma coisa?\n1- Vender passagem.\n2- Cancelar compra.\n3- Mostrar mapa de ocupação.\n4- Sair.\nSua opção: ')).strip()
    print(50 * '=')
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
        opcao = input("Opção inválida! Digite apenas 1, 2, 3 ou 4: ").strip()
