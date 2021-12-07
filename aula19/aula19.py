"""
while em Python
utilizando para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

#while True:       # loop infinito / While = enquanto
#   nome = input('Qual seu nome? ')
#    print(f'Olá {nome}!')

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue   # break para o laço

    print(x)
    x = x + 1

print('Acabou!')

#################################################################
a = 0  # coluna
while a < 10:
    b = 0  # linha

    while b < 5:
        print(f'({a},{b})')
        b += 1

    a += 1
print('Acabou!')

#################################################################

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido!')



























