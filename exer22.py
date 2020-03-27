'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
'''
# 1ª versão
import math 

angulo = float(input('Digite um valor para o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('\nO seno de {} é {:.2f}.\n'.format(angulo, seno))
print('O cosseno de {} é {:.2f}.\n'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}.'.format(angulo, tangente))

# 2ª versão
from math import radians, sin, cos, tan

angulo = float(input('Digite um valor para o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('\nO seno de {} é {:.2f}.\n'.format(angulo, seno))
print('O cosseno de {} é {:.2f}.\n'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}.'.format(angulo, tangente))