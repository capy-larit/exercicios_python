distancia = int(input('Digite a distância em metros: '))
tempo = int(input('Digite o tempo em segundos: '))

velocidade_media = distancia/tempo

print(
f"""Vm em m/s: {velocidade_media} 
Vm em km/h: {velocidade_media * 3.6}"""
)