"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#numero_inteiro = input('Digite um número inteiro: ')
#if numero_inteiro.isdigit():
#    numero_inteiro = int(numero_inteiro)
#    if numero_inteiro % 2 == 0:
#        print(f'{numero_inteiro} é par')
#    else:
#        print(f'{numero_inteiro} é ímpar.')
#else:
#    print('Isso não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usúario e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

"""
horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horário de estar entre 0 e 23 horas.')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')

else:
     print('Por favor, digite um horário entre 0 e 23.')