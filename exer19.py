'''
Faça um algoritmo receba um número e diga qual é o seu antecessor e sucessor. 
'''

num = int(input('Digite um número: '))

print(
  'Analisando o valor {}, seu antecessor é {} e {} é o seu sucessor.'.format(num, num - 1, num + 1)
)
