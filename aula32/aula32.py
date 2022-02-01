"""
função - def em Py (parte 1) e (parte 2)
"""

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Raquelle')

#########################################
## não se usa print dentro da função, geralmente é o return


def funcao (var):
    print(var)

variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor.')


###############################
def divisao(ni, n2):
    return ni/ n2

divide = divisao(8,2)
if divide:
    print(divide)
else:
    print('conta inválida.')

