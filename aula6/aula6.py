"""
Váriaveis -> Iniciar com letra, pode conter números, separa _, letras minusculas
"""
nome = 'Isaac'
idade = 30
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2


print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maior de Idade?', e_maior)
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)