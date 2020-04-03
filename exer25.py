'''
Faça um programa de empréstimo para funcionários com desconto em folha. O valor da prestação não pode ultrapassar 30% do salário bruto do funcionário. Faça um programa em Python que solicite o valor do salário bruto, o valor da prestação e informe se o empréstimo pode ou não ser concedido
'''

salario_bruto = float(input('Digite o salário bruto: '))

limite = salario_bruto * 0.30

if (salario_bruto <= 0):
  print('Salário Inválido! Tente novamente sendo o valor do salário bruto maior que zero.')

else:
  valor_prestacao = float(input('Digite o valor da prestação: '))
  if(valor_prestacao <= 0 ):
    print('Valor da prestação inválida! Tente novamente sendo o valor da prestação maior que zero.')
      
  else:
    limite = salario_bruto * 0.30

    concedido = valor_prestacao <= limite

    if (concedido):
      print('Empréstimo concedido!')

    else:
      print('Empréstimo não concedido')

print('\nTerminou !')