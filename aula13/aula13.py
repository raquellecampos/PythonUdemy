usuario = input('Digite seu usuário: ')
qtd_caractere = len(usuario)

#  print(usuario, qtd_caractere, type(qtd_caractere))

if qtd_caractere < 6:
    print('Você precisa pelo menos digitar 6 caracteres!')
else:
    print('Você foi cadastrado no sitema!')


    string1 = input('Digite alguma coisa: ')
    string2 = input('Digite outra coisa: ')

    print(f'A quantidade de caractere digitados foi {len(string1) + len(string2)}')

    #  em python tudo é um objeto

    print(string2.__len__())