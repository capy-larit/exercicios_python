'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot

co = float(input(
  'Digite um valor para o cateto oposto: '
))

ca = float(input(
  'Digite um valor para o cateto adjacente: '
))

print(f'A hipotenusa é {hypot(co, ca)}'.replace('.',','))