'''
Documentação e funções built-in úteis
'''

num1 = input('Digite um número: ')   #input retorna string
num2 = input('Digite outro número: ')

#num1 = int(num1)   #tenho que coverter para int
#num2 = int(num2)

#print(num1 + num2)

#  isnumeric  isdigit  isdecimal
#  números e positivos (12345)
#print(num1.isnumeric())
#print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

else:
    print('Não pude converter.')



