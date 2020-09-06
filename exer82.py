"""
Faça um programa em Python que preencha uma lista com dez números reais
informados pelo usuário, calcule e mostre a quantidade de números negativos e a
soma dos positivos dessa lista.
"""

lista = []
contNegativos = soma = 0
for i in range(1, 11):
    num = float(input(f'Informe o {i}º número real: '))
    lista.append(num)
    if num < 0:
        contNegativos += 1
    else:
        soma += num
print(50 * '=')
print(
f'A quantidade de números negativos: {contNegativos}\nSoma dos números positivos: {soma}'
)
