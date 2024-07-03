# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.


lista_num = [1,2,3,4,5,6,7,8,9,10]
print (lista_num)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela


lista_frutas = ['abacaxi', 'maçã', 'laranja', 'abacate', 'banana']
print (lista_frutas)


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

string_um = ['A vida é bela, ']
string_dois = [' a gente é que caga nela.']
string_tres = string_um + string_dois
print(string_tres)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla_num = (1, 2, 2, 3, 4, 4, 4, 5)
list_tupla = [1, 2, 2, 3, 4, 4, 4, 5]
contagem_lista = list_tupla.count(4)
print (contagem_lista)

# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario_vazio = {}
print(dicionario_vazio)


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dicionario_cheio = {'Wilmara': 31,'João': 29,'Joaquim': 32, 'Maria': 41}
print (dicionario_cheio)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dicionario_cheio = {'Wilmara': 31,'João': 29,'Joaquim': 32, 'Maria': 41}
dicionario_cheio["Marcelo"] = 23
print(dicionario_cheio)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dict_chaves = {
    'Lapis': 23,
    'Caderno': [54, 56],
    'Prancheta': 65
}
print(dict_chaves)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lista_elementos =  [
    'Quero amor maior do mundo', 
    (1,2),
    {'Maria Antonia': 26, 'Caio': 29},
    1,23
]
print (lista_elementos)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[1:18])