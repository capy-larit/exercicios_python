'''
Faça um algoritmo em Python para ler o nome, as três notas e o número de faltas de um aluno e escrever qual a sua situação final: Aprovado, Reprovado por Falta ou Reprovado por Média.  

A média para aprovação é 7,0 e o limite de faltas é 25% do total de aulas. 

O número de aulas ministradas no semestre foi 80. A reprovação por falta sobrepõe a reprovação por Média.
'''

nome = input('Digite o nome: ').lower().split()
nota = float(input('Digite a primeira nota: '))
nota_1 = float(input('Digite a segunda nota: '))
nota_2 = float(input('Digite a terceira nota: '))
qtd_faltas = int(input('Digite a quantidade de faltas: '))

total_nota = nota + nota_1 + nota_2

if nota < 0.0 or nota_1 < 0.0 or nota_2 < 0.0:
  print('Valores negativos não são aceitos.')

elif nota > 10.0 or nota_1 > 10.0 or nota_2 > 10.0:
  print('Não existe nota maior que 10 nessa instituição.')

elif total_nota >= 7.0 and qtd_faltas <= 20:
  print('Aprovado!')

elif total_nota >= 7.0 and qtd_faltas > 20:
  print('Reprovado por Falta.')
 
elif total_nota < 7.0 and qtd_faltas > 20:
  print('Reprovado por Falta.')

elif total_nota < 7.0 and qtd_faltas <= 20:
  print('Reprovado por Média.')
