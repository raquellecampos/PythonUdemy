"""

Opreradores Relacionais
== > >= < <= !=
"""

num_1 = 2
num_2 = 2

print(num_1 == num_2)

num_3 = 5
num_4 = 6

expressao = (num_3 > num_4)
print(expressao)

espressao2 = (num_3 <= num_4)
print(espressao2)

var_1 = 'Isaac'
var_2 = 'Henrique'

espressao3 = (var_1 != var_2)
print(espressao3)

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

idade = int(idade)


#  Limite para pegar emprestimo
idade_menor = 18
idade_maior = 50

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} não pode pegar empréstimo')