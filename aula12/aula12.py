"""
Operadores Lógicos
and = 'E'
or = 'Ou'
not = 'Negação'
in = 'está em'
not in = 'Não está em'
"""

a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

c = ''
d = 0

if not c:
    print('Por favor, preencha o valor de C.')

nome = 'Anna Luísa.'

if 'na' in nome:  # Not in = não está em...
    print('Existe.')
else:
    print('Não existe.')

    ###############################################

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Isaac'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')