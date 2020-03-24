'''
Faça um programa em Python que:
a) Receba do usuário os dados de um produto específico: 
- Preço unitário;
- País de origem (1-Brasil, 2-México,3-Outros);
- Meio de Transporte (T-Terrestre, F-Fluvial, A-Aéreo); 
- Carga Perigosa (S-Sim, N-Não). 

b) O algoritmo deve calcular: 
- Valor do Imposto;
- Valor do Transporte; 
- Valor do Seguro.

Regras para cálculo do valor do imposto: 
- Percentual de imposto sobre o preço unitário de até R$ 100,00: 5%;
- Percentual de imposto sobre o preço unitário maior que R$ 100,00: 20%.

Regras para cálculo do valor do transporte:
- Caso a carga seja perigosa de origem do país 1 o valor do transporte será R$ 21,00;
- Caso a carga seja perigosa de origem do país 2 o valor do transporte será R$ 27,00;
- Caso a carga seja perigosa de origem do país 3 o valor do transporte será R$ 50,00;
- Caso a carga não seja perigosa com origem do país 1 o valor do transporte será R$ 21,00;
- Caso a carga não seja perigosa com origem do país 2 o valor do transporte será R$ 25,00;
- Caso a carga não seja perigosa com origem do país 3 o valor do transporte será R$ 40,00.

Valor do Seguro: 
- Os produtos que vem do México e os produtos que utilizam transporte aéreo pagam metade do valor do seu preço unitário como seguro. Os demais produtos não pagam seguro. 

c) Mostrar na tela:
- Preço final (preço unitário + impostos + valor do transporte + seguro).
'''

preco_unitario = round(
  float(input(  'Digite o preço unitário: ')),2
)
pais_origem = int(input('Digite o país de origem: '))
meio_transporte = input('Digite o meio de transporte: ').lower()
carga_perigosa = input(
  'Informe se a carga é perigosa (sim ou não): '
).lower()
imposto = preco_unitario * 0.05
imposto_maior = preco_unitario * 0.2
valor_total = 0

if preco_unitario <= 100:
  valor_total += imposto

elif preco_unitario > 100:
  valor_total += imposto_maior

if pais_origem == 1 and carga_perigosa == 'sim':
  valor_total += 21.00

elif pais_origem == 2 and carga_perigosa == 'sim':
  valor_total += 27.00

elif pais_origem == 3 and carga_perigosa == 'sim':
  valor_total += 50.00

elif pais_origem == 1 and carga_perigosa =='não':
  valor_total += 21.00

elif pais_origem == 2 and carga_perigosa == 'não':
  valor_total += 25.00

elif pais_origem == 3 and carga_perigosa == 'não':
  valor_total += 40.00

if (
    pais_origem == 2 
    and meio_transporte == 'a' 
    and preco_unitario <= 100
):
  print(valor_total + (preco_unitario/2))

elif (
    pais_origem == 2 
    and meio_transporte == 'a' 
    and preco_unitario > 100
):
  print(valor_total + (preco_unitario/2))

else:
  print(valor_total + preco_unitario)


