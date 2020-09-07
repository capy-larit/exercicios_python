"3"
def maior_valor(tupla):
    return max(tupla)

"4"
def retornar_media(tupla):
    return sum(tupla) / len(tupla)

"5"
def maior_string(tupla):
   maior = tupla[0] #Banana
   maiorString = len(tupla[0]) #6
   for i in tupla:
      if len(i) > maiorString:
         maior = i
   return(maior)


"""
1. Crie uma tupla de números inteiros positivos com valores que você quiser,
   no mínimo 15 valores.
"""

numeros = (12, 14, 16, 15, 29, 18, 19, 1, 129, 167, 34, 45, 56, 78, 90, 100)

"2. Imprima todos os números da tupla anterior na tela, um de cada vez."

for i in numeros:
    print(i)

"""
3. Faça uma função que recebe uma tupla de números inteiros e retorna o maior
   valor contido dentro da tupla.
"""

maior = maior_valor(numeros)
print(f"O maior valor é: {maior}")

"""
4. Faça uma função que recebe uma tupla de números reais e retorna a média
   aritmética de todos os valores contidos dentro da tupla.
"""

numeros_reais = (4.5, 9.2, 7.8, 5.6, 8.9)
media = retornar_media(numeros_reais)
print(f"A média é: {media}")

"""
5. Faça uma função que recebe uma tupla de Strings e retorna a maior String de
   todos os valores contidos dentro da tupla.
"""

frutas = ("Banana", "Maça", "Uva", "Lichia", "Morango")
string_maior = maior_string(frutas)
print(f"A maior String é: {string_maior}")
