# Crie um cadastro de clientes para uma loja de bebidas
# o cadastro deve solicitar ao usuário:
# Nome,sobrenome e idade
# o sistema deve permitir apenas clientes maiores de idade
# caso a idade seja menor ,informar que não pode ser cadastrado


print('*'*10,   'Cadastro de Clientes', '*'*10)
print('\n')

nome =input('digite seu nome: ')

sobrenome =input('seu sobrenome:')

idade =int(input('digite sua idade:'))

if(idade >=18):
    print('Cadastrado com susseso !')
elif(idade >0):
    print('Não permitido menores de idade')
else :
    print('Idade informada é invalida')        
    