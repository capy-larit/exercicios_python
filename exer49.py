'''
Faça um programa em Python que leia 50 idades e mostre na tela a media simples das idades digitadas.
Observações:
- Não aceitar idade < 0;
- Necessariamente precisa ter 50 idades válidas.
'''

cont = 0
soma = 0
idade = 0

while cont < 50:
    idade = int(input('Digite uma/outra idade: '))
    while idade < 0:
        print('Digite uma idade válida.')
        idade = int(input('Digite uma/outra idade: '))
    soma += idade
    cont += 1
print('A média das idades digitadas é {}'.format(soma / 50))
