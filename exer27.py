'''
Faça um programa em Python que solicite o número da conta (com 3 dígitos) e calcule o dígito verificador. 

Os passos para calcular o dígito verificador são: 

Ex: Número da conta = 235. 

1) Somar o número da conta com o seu inverso. 

>>> Ex: 235 + 532 = 767.

2) Multiplicar cada digito do número obtido no passo anterior pela sua ordem posicional e somar esses resultados. O último digito do número obtido é o dígito verificador.  

>>> Ex: 7 x 1 + 6 x 2 + 7 x 3 = 40 (dígito verificador >>> 0). 

• PS: Use o operador % e a divisão inteira para obter o dígito verificador. 
'''

numero_conta = input(
  'Digite o número da sua conta bancária: '
)

reversed(numero_conta)
inverso =''.join( reversed(numero_conta) )

soma = int(numero_conta) + int(inverso)

if soma >= 100 and soma <= 999:
  digito_0 = soma // 100 % 10

  digito_1 = soma // 10 % 10

  digito_2 = soma // 1 % 10

  soma_digito =  digito_0 * 1 + digito_1 * 2 + digito_2 * 3 

  digito_verificador = soma_digito % 10
  
  print('O dígito verificador dessa conta bancária é', digito_verificador)

else:
  print('O número da conta bancária deve ter três dígitos. Ex: 123.')
