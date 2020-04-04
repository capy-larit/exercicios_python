'''
Faça um algoritmo em Python para ler três valores reais e informar se estes podem ou não formar os lados de um triângulo e qual tipo de triângulo seria: equilátero, isósceles ou escaleno.
'''

a = int(input('Digite o valor para o primeiro lado: '))
b = int(input('Digite o valor para o segundo lado: '))
c = int(input('Digite o valor para o terceiro lado: '))

if a <= 0 or b <= 0 or c <=0 :
  print("Lados nulos ou negativos não são aceitos.")
  
elif not(a < b + c and c < a + b and b < a + c):
  print("Triangulo inexistente.")

elif a <= 0 or b <= 0 or c <=0 :
  print("Lados nulos ou negativos não são aceitos.")

elif a == b and a == c and b == c:
  print('Esses valores formam um triângulo equilátero.')

elif a == b or a == c or b == c:
  print('Esses valores formam um triângulo isósceles.')
  
else:
  print('Esses valores formam um triângulo escaleno.')