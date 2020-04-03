'''
Faça um programa para uma companhia aérea que solicite o destino e se o cliente deseja somente ida ou ida e volta.

Valores:
Norte - Ida: R$ 280 - Ida e volta = R$ 400;
Nordeste - Ida: R$ 380 - Ida e volta = R$ 628;
Centro-Oeste - Ida: R$ 620 - Ida e volta: R$ 1100.

Obs: A empresa não trabalha nos trechos sul e sudeste.
'''

import re

destino = input('Digite o seu destino: ').lower().strip()
ida_volta = input(
  'Informe se deseja passagem somente de ida ou de ida e volta: '
).lower().strip()

if destino == 'norte' and ida_volta == 'ida':
  print('Sua passagem custará R$ {}.\nObrigada por escolher a nossa companhia!'.format(280))

if destino == 'norte' and ida_volta == 'ida e volta':
  print('Suas passagens custarão R$ {}.\nObrigada por escolher a nossa companhia!'.format(400))

if destino == 'nordeste' and ida_volta == 'ida':
  print ('Sua passagem custará R$ {}.\nObrigada por escolher a nossa companhia!'.format(380))

if destino == 'nordeste' and ida_volta == 'ida e volta':
  print('Suas passagem custarão R$ {}.\nObrigada por escolher a nossa companhia!'.format(628))

if re.search('centro\soeste|centro-oeste', destino) and ida_volta == 'ida':
  print('Sua passagem custará R$ {}.\nObrigada por escolher a nossa companhia!'.format(620))

if re.search('centro\soeste|centro-oeste', destino)  and ida_volta == 'ida e volta':
  print('Suas passagens custarão R$ {}.\nObrigada por escolher a nossa companhia!'.format(1100))

elif destino == 'sul' or destino == 'sudeste':
  print('Desculpe, mas a nossa empresa não trabalha nos trechos Sul e Sudeste do país.')
