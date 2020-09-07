def chamar_menu(tipo_defeitos):
    print('\n# Tipos de Defeitos #\n')
    for i in range(1, 5):
        print(f'{tipo_defeitos[i]}')
    defeito = int(input('\n \nDigite o tipo de defeito: '))
    return defeito
