'''
Elabore um algoritmo em Python que indique se um número digitado está compreendido entre 0 e 30 ou entre 40 e 79 ou fora dos limites estabelecidos
'''

numero = int(input('Digite um número: '))

if numero >= 0 and numero <= 30:
  print(
    'O número {} está dentro do intervalo de 0-30.'.format(numero)
  )

if numero >= 40 and numero <= 79:
  print(
    'O número {} está dentro do intervalo de 40-79.'.format(numero)
  )

else:
  print(
    'O número digitado está fora dos limites estabelecidos.'
  )