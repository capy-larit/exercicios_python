salario_inicial = float(input('Digite o seu salário inicial: '))
salario_aumento = float(input('Digite o seu salário com o aumento: '))

diferenca = salario_aumento - salario_inicial
percentual = (diferenca / salario_inicial) * 100

print(f'Aumento Percentual: {percentual}%')

