candidato_A = int(input(
  "Digite a quantidade de votos do canditado A: "
))

candidato_B = int(input(
  "Digite a quantidade de votos do candidato B: "
))

candidato_C = int(input(
  "Digite a quantidade de votos do candidato C: "
))

quantidade_brancos = int(input(
  "Digite a quantidade de votos em branco: "
))

quantidade_nulos = int(input(
  "Digite a quantidade de votos nulos: "
))

total_eleitores = (
  candidato_A + candidato_B + candidato_C + quantidade_brancos + quantidade_nulos
)

percentual_votos_A = candidato_A / total_eleitores * 100

percentual_votos_B = candidato_B / total_eleitores * 100

percentual_votos_C = candidato_C / total_eleitores * 100

percentual_votos_brancos = (
  quantidade_brancos / total_eleitores * 100
)

percentual_votos_nulos = (
  quantidade_nulos / total_eleitores * 100 
)

saida = f"""
Quantidade total de eleitores: {total_eleitores}

Percentual de votos candidato A: {percentual_votos_A:.02f}%

Percentual de votos candidato B: {percentual_votos_B:.02f}%

Percentual de votos candidato C: {percentual_votos_C:.02f}%

Percentual de votos Brancos: {percentual_votos_brancos:.02f}%

Percentual de votos Nulos: {percentual_votos_nulos:.02f}%
""".replace('.', ',')

print(saida)



