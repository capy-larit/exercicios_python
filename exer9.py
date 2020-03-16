preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto: ')) / 100
valor_desconto = preco * desconto

print(
  f"""
  {'=' * 50}
  Valor do desconto: R$ {valor_desconto:.2f}
  Novo preço: R$ {preco - valor_desconto:.2f}
  {'=' * 50}
  """.replace('.' , ',')
)