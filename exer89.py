"""
Crie um dicionário com os nomes de 5 filmes como chave e como valor outro
dicionário contendo o ano em que o filme foi lançado e o ator principal.
"""

filmes = {
    'Cinderela': {'Ano' : 2017, 'Ator' : 'Jack Nicholson'},
    'O Diário da Princesa' : {'Ano' : 2001, 'Ator' : 'Anne Hathawat'},
    'Minions' : {'Ano' : 2015, 'Ator' : 'Minion'},
    'The Old Guard' : {'Ano' : 2020, 'Ator' : 'Charlize Theron'},
    'Parasita' : {'Ano' : 2019, 'Ator' : 'Cho Yeo-jeong'}
}
for filme, info in filmes.items():
    print(f'\nFilme: {filme}\nAno: {info["Ano"]}\nAtor: {info["Ator"]}')
