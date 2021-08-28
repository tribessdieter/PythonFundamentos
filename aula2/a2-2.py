# Curso : python Fundamentos proway
#  AULA : DIA 2- PARTE 2
# ASSUNTO : LAÇO DE REPETICÃO WHILE, INSTRUÇOES ANINHADAS
# DATA : 2021-08-28

# repeticoes = 0
# while(repeticoes <=3): #enquanto
#     idade = input('digite a idade :')
#     repeticoes = repeticoes +1



# print('*'*10,   'Cadastro de Clientes', '*'*10)
# print('\n')

# nome =input('digite seu nome: ')

# sobrenome =input('seu sobrenome:')

# idade =int(input('digite sua idade:'))

# invalido = True
# while(invalido):
#     if(idade >=18):
#         print('Cadastrado com susseso !')
#         invalido = False
#     elif(idade >0):
#         print('Não permitido menores de idade')
#         invalido = False
#     else :
#         print('Idade informada é invalida')   
#         idade =int(input('digite sua idade:'))


import os

invalido = True
while(invalido):
            
    print('*'*10,   'Cadastro de Bebidas', '*'*10,'\n')
    print('\t-Cadastrar uma Bebida')
    print('\t-2-Listar bebidas cadastradas')
    print('\t0-sair')
    opcao = int(input('\nDigite uma opção do menu :'))

    if(opcao < 0 or opcao >2):
        print('Opção invalida !')
        input('Digite enter para continuar...')
        os.system('clear')
    else:
        invalido= False



        