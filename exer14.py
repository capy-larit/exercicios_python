total_a_vista = float(input('Digite o valor total à vista: '))
cada_parcela = float(input('Digite o valor das parcelas: '))

parcela_10 = cada_parcela * 10
total_parcelado = parcela_10 - total_a_vista
percentual = (total_parcelado / total_a_vista) * 100

print(f'O desconto concedido foi de {percentual}%')