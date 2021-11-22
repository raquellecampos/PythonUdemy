"""
Entrada de dados
"""
# nome = input("Qual seu nome? ")
# print(f'O usuário digitou {nome} e o tipo da variável é '
#      f'{type(nome)}')

nome = input("Qual seu nome? ")
idade = input("Qual seua idade? ")
ano_nascimento = 2021 - int(idade)

print()
print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}.')

numero_1 = int(input('Digite um número: '))  #Type cast
numero_2 = input('Digite outro número: ')
numero_2 = int(numero_2)

print(numero_1 + numero_2)
