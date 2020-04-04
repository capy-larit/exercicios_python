'''
Elabore um programa em Python para testar se uma senha digitada pelo usuário é igual a 1214. Se a senha estiver correta mostre na tela: "Acesso permitido", do contrário emita a mensagem: "Você não tem acesso ao sistema".
'''

senha = input('Digite a senha: ')

if senha == '1214':
  print('Acesso permitido.')

else:
  print('Você não tem acesso ao sistema.')