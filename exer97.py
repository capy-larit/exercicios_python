"""
Faça um programa em Python que solicite ao usuário 10 números inteiros diferentes.
Mostrar na tela quantos números foram digitados respeitando a solicitação.
Observação: O usuário somente poderá digitar 10 números.
"""

lista = []
try:
    for i in range(10):
        numero = int(input(f'Digite o {i + 1}º número: '))
        while numero in lista:
            print('Já digitou esse número. Tente novamente.')
            numero = int(input(f'Digite o {i + 1}º número: '))
        lista.append(numero)
except:
    print('Deve ser um número inteiro')
    exit()
print(f'Quantidade de números digitados: {len(lista)}')
print(lista)
