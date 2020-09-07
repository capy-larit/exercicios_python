from exer91_chamar_menu import chamar_menu

def registrar(dic, tipo_defeitos):
    try:
        id = int(input('\nDigite um número de identificação ou 0 para sair: '))
        if id in dic:
            print('\nEsse número de identificação já existe.')
        elif id == 0:
            print(f'\nQuantida de mouses: {len(dic)}')
            print(f'{"Situação": <45} {"Quantidade": <20} {"Percentual": >10}')
            values_dic = list(dic.values())
            for i in range(1 , 5):
                if len(dic) == 0:
                    print(f'{tipo_defeitos[i]: <54} {values_dic.count(i): <18} {0}%')
                else:
                    print(f'{tipo_defeitos[i]: <54} {values_dic.count(i): <18} {(values_dic.count(i) * 100) / len(dic):.0f}%')
            exit()
        else:
            defeito = chamar_menu(tipo_defeitos)
            while defeito not in tipo_defeitos:
                print('\nNão é uma opção de defeito. Tente novamente use os números (1, 2, 3, 4)')
                defeito = chamar_menu(tipo_defeitos)
            dic[id] = defeito
    except ValueError:
        print('DEVE SER UM NÚMERO')
