"""
For in em Python
Iterando strings com for
função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

for letra in texto:
    print(letra)

########################################
for numero in range(0,100,8):
    print(numero)

print('#########')

for numero in range(100):
    if numero % 8 == 0:
        print(numero)


###########################################
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        # break
    else:
        nova_string += letra

print(nova_string)

# continue - pula pro proximo laço
# break - para o laço