"""

Condições IF, ELIF e ELSE
"""

if False:
    print("Verdadeiro.")
    print('teste')
elif True:  #só é executado se a primeira for falsa
    print('Agora é verdadeiro')
    nome = input('Qual seu nome? ')

    print(f'Seu nome é {nome}')
elif False:
    print('mais uma verdadeira.')
    print(22 + 22)
else:
    print('A minha expressão não é verdadeira.')
    print('Olá!')