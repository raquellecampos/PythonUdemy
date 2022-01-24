"""

FOR/ ELSE em Python
"""

variavel = ['Raquelle', 'Isaac', 'Anna']

comeca_com_i = False
for valor in variavel:
    if valor.lower().startswith('i'):  ##Começa com...
        comeca_com_i = True

if comeca_com_i:
    print('Existe')
else:
    print('Não existe')