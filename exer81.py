"""
Faça um programa em Python que receba o total de vendas de cada vendedor de
uma loja e armazene-as em uma lista. Receba também o percentual de comissão a
que cada vendedor tem direito e armazene-os em outra lista. Receba os nomes
desses vendedores e armazene-os em uma terceira lista.
Observação: Existem apenas 10 vendedores na loja.
Calcule e mostre:
a) Um relatório com os nomes dos vendedores e os valores a receber referentes
à comissão;
b) O total das vendas de todos os vendedores;
c) O maior valor a receber e o nome de quem o receberá;
d) O menor valor a receber e o nome de quem o receberá;
"""

total_vendas = []
percentual_comissao = []
nomes_vendedores = []
comissao = []
nomeMenorVendedor = nomeMaiorVendedor = 'OK'
maior_valor = menor_valor = soma_vendas = 0
for i in range(10):
    print(27 * '=', f'Informações do {i + 1}º vendedor', 27 * '=')
    nomes_vendedores.append(input('Nome: '))
    total_vendas.append(int(input('Total de vendas: ')))
    percentual_comissao.append(int(input('Percentual de Comissão: ')) / 100)
    comissao.append(total_vendas[i] * percentual_comissao[i])
    if i == 0:
        maior_valor = menor_valor = comissao[i]
    else:
        if comissao[i] > maior_valor:
            maior_valor = comissao[i]
            nomeMaiorVendedor = nomes_vendedores[i]
        elif comissao[i] < menor_valor:
            menor_valor = comissao[i]
            nomeMenorVendedor = nomes_vendedores[i]
print('\n')
print(25 * '=', 'Relatório dos Vendedores', 25 * '=')
for i in range(len(nomes_vendedores)):
    print(f'\tNome: {nomes_vendedores[i]}\t\t\t\tValor da Comissão: {comissao[i]}')
print(76 * '=')
print(f'O total de vendas: {sum(total_vendas)}')
print(76 * '=')
print(f'O maior valor a ser recebido é {maior_valor} de {nomeMaiorVendedor}\nO menor valor a ser recebido é {menor_valor} de {nomeMenorVendedor}')
