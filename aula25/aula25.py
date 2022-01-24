"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

##iterar
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que mais apareceu é {palavra} ({contagem}x)')  ##quantas vezes uma palavra apareceu na frase

#######################################
####Join

string = "O Brasil é penta."
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(string2)
print(lista)

##############Enumerate
string = "O Brasil é penta."
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])