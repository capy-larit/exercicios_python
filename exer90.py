"""
Faça uma função em Python que receba o RA do aluno e retorne se ele está ativo ou não.
Observação: Os RAs dos alunos matriculados estão guardados em um dicionário.
"""

def receber(dic):
    ra = input('Digite o RA: ')
    if ra in dic.values():
        print('Esse RA está ativo.')
    else:
        print('Esse RA NÃO está ativo.')


dic = {
    'ra' : '2001',
    'ra' : '2002',
    'ra' : '2003',
    'ra' : '2004',
    'ra' : '2005',
    'ra' : '2006',
    'ra' : '2007',
    'ra' : '2008',
    'ra' : '2009',
    'ra' : '2010'}
receber(dic)
