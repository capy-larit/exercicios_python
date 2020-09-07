"""
Faça uma função em Python que retorna o maior e a posição do maior número numa
lista.
"""

def maior(lista):
    return(print(f'O maior número da lista é {max(lista)} e a posição dele é {lista.index(max(lista))}.'))


numeros = [1, 20, 36, 45, 54, 9, 12, 30, 105, 67]
maior(numeros)
