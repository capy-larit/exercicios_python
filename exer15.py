"""
Escreva um algoritmo para um estacionamento que seja capaz de exibir o valor que o cliente deve pagar pelo tempo que seu veículo ficou estacionado.
Regras para carro e moto:
Até 15 minutos não paga.
Regras para carro:
De 16 até 180 minutos pagará R$ 20,00;
A partir de 180 minutos, pagará R$ 0,15 por minuto adicional.
Regras para moto:
De 16 até 180 minutos pagará R$ 17,00;
A partir de 180 minutos, pagará R$ 0,10 por minuto adicional.
"""


# '.lower()' serve para tornar a string em letra minúscula
veiculo = input('Informe qual é o seu veículo: ').lower()
minutos = int(input('Informe o tempo em minutos: '))
valor_carro = 20.00
valor_moto = 17.00
extra_carro = float((minutos - 180) * 0.15)
extra_moto = float((minutos - 180) * 0.10)

#'range' gera uma lista de valores a partir de 0 ou do valor # especificado
# 'in' verifica se um dado está dentro da lista de dados

if veiculo in ['carro','moto'] and minutos in range(16):
  print('Valor: R$ 0,00')

elif veiculo == 'carro' and minutos in range(16, 181):
  print('Valor: R$ 20,00')

elif veiculo == 'moto'and minutos in range(16, 181):
  print('Valor: R$ 17,00')

elif veiculo == 'carro' and minutos >= 181:
  print('R$', (valor_carro + (extra_carro)))

elif veiculo == 'moto' and minutos >= 181:
  print('R$', (valor_moto + (extra_moto)))