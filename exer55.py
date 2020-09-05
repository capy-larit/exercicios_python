"""
A sequência de números de Fibonacci é a seguinte: os dois primeiros termos
têm o valor 1 e cada termo seguinte é igual à soma dos dois anteriores.
1, 1, 2, 3, 5, 8, 13, 21, ...
Escreva um programa em Python que solicite ao usuário o número de termos da
sequência de Fibonacci e calcule o valor desse termo. Por exemplo, se o
número fornecido pelo usuário for 7, o programa deverá encontrar e imprimir o
valor 13.
Obrigatório usar laço while.
"""

numeroUsu = int(input('Digite um número: '))
num1 = 0
num2 = 1

for i in range(3, numeroUsu + 2):
    soma = num1 + num2
    num1 = num2
    num2 = soma
print('O número na posição escolhida é {}.'.format(soma))
