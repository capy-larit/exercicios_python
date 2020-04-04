'''
Faça um programa que receba a três notas (Trabalho de Laboratóri, Avaliação Semestral e Exame Final), calcule e mostre a média ponderada e o conceito conforme as tabelas:

Pesos:
 Trabalho de Laboratório - peso 2; 
 Avaliação Semestral - peso 3; 
 Exame Final - peso 5.

Média Ponderada:
 de 8,0 a 10,0 - Conceito A; 
 de 7,0 a 7,9 - Conceito B; 
 de 6,0 a 6,9 - Conceito C; 
 de 5,0 a 5,9 - Conceito D; 
 de 0,0 a 4,9 - Conceito E.
'''

nota_lab = float(input(
  'Digite a nota do trabalho de laboratório: '
))
nota_semestral = float(input(
  'Digite a bota da avaliação semestral: '
))
nota_exame = float(input('Digite a nota do exame final: '))


media_ponderada = (2 * nota_lab + 3 * nota_semestral + 5 * nota_exame) / (2 + 3 + 5)


if nota_lab < 0 or nota_semestral < 0 or nota_exame < 0:
  print('Nota inválida!')

elif media_ponderada >= 0.0 and media_ponderada <= 4.9:
  print(
    'Você obteve conceito E, pois sua média foi {}.\nEstude mais!'.format(media_ponderada)
  )

elif media_ponderada >= 5.0 and media_ponderada <= 5.9:
  print(
    'Você obteve conceito D, pois sua média foi {}.\nEstude mais!'.format(media_ponderada)
  )

elif media_ponderada >= 6.0 and media_ponderada <=6.9:
  print(
    'Você obteve conceito C, pois sua média foi {}.\nEstude mais!'.format(media_ponderada)
  )

elif media_ponderada >= 7.0 and media_ponderada <= 7.9:
  print(
    'Você obteve conceito B, pois sua média foi {}.\nParabéns! Continue estudando :)'.format(media_ponderada)
  )

elif media_ponderada >= 8.0 and media_ponderada <= 10.0:
  print(
    'Você obteve conceito A, pois sua média foi {}.\nParabéns! Continue assim! :)'.format(media_ponderada)
  )

