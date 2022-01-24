"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
mim, max
range
"""

#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#    -    5    4    3    2    1
lista[2] = 'Raquelle'

print(lista[0:4])  # posso excluir o 0.
print(lista[2])
print(lista)
print(lista[-1])  # último objeto da lista


lista1 = [1,2,3]
lista2 = [4,5,6]

lista1.extend(lista2)  # lista1 extende a lista2
lista2.append('b')   # insere um valor no final da lista
lista2.insert(0, 'banana')  # insere um valor no local do índice indicado
lista1.pop()  # remove o último elemento da lista
del(lista2[0]) # remove um trecho da lista por fatiamento
print( max(lista2))
print( min(lista2))


print(lista1)
print(lista2)

################################################

###objeto iteravel = repetir, reiterar / for

#l2 = list(range(0,100,8))
l2 = [0,1,2,3,4,5,6,7,8,9]
for valor in l2:
    print(valor)











