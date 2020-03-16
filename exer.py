idade = int(input('Informe sua idade: '))

# se a pessoa tem menos de 16 anos não pode votar
if idade < 16:
  print('Você não pode votar')

# se a pessoa tiver 16 anos ou mais e menos que 18 
# então ela pode votar
elif idade >= 16 and idade < 18:
  print('Você pode votar')

# se a pessoa tiver entre 18 até 70 anos
# ela é obrigada a votar
elif idade >= 18 and idade <= 69:
  print('Você é obrigado a votar')

# caso a pessoa tenha mais que 70 anos
else:
  print('Você não precisa votar')

