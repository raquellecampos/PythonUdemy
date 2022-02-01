"""
Função (Def) - *args **kwargs -
parte 3
"""

# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6
#
# var = func(1,2,3,4,5, nome='Raquelle', a6='5')
# print(var[0], var[1])

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome='Raquelle', sobrenome='Campos')

variavel = 'valor'  # escopo global

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'  # escopo local
    print(variavel)

func()
func2()

print(variavel)  # escopo global