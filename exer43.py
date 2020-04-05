'''
Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. 
 
Elabore um algoritmo em Python que leia o valor do produto e mostre na tela o valor de venda para o produto.
'''

valor_produto = float(input('Digite o valor do produto: '))

if valor_produto <= 20:
  print(
    'O valor de venda é R$ {}.'.format((valor_produto * 1.45
  )))

else:
  print(
    'O valor de venda é R$ {}.'.format((valor_produto * 1.30
  )))
