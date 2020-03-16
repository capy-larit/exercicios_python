# ".strip()" é um método de ignorar os espaços que o  usuário digitar
x = input('Digite um número de 0 à 99: ').strip()

if len(x) > 2:
  print('Apenas números de dois dígitos são aceitos')

else:
  x = int(x)
  dezena = x // 10 
  unidade = x - dezena * 10 
  print(f'Dezena: {dezena}\nUnidade: {unidade}')