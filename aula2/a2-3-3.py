lista = ['dieter']
lista2 = ('dieter')
dicionario = {'nome':'dieter','sobrenome' : 'tribess', 'idade': 42}

lista[0]
lista2[0]
 
# Alterando dados de um dicionario 

print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade']) 

# Alterando dados de um dicionario
dicionario['nome']
dicionario['sobrenome']
dicionario['idade'] = 42

#lendo os dados alterados
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# adicionar um novo conjunto de chaves : valor
dicionario['cpf'] = '00371901995'
print(dicionario['cpf'])

cliente = {}
cliente2 = {'nome' :'', 'sobrenome' :'','idade' :42}

cliente['nome'] =input('digite o nome: ')
cliente['sobrenome'] = input('digite o sobrenome: ' )
cliente['idade'] = int(input('digite a idade: '))

print(cliente)
# deletar uma chave de um dicionario
del(cliente['idade'])
print(cliente)


cliente2['nome'] =input('digite o nome: ')
cliente2['sobrenome'] = input('digite o sobrenome: ' )
cliente2['idade'] = int(input('digite a idade: '))

clientes = [cliente,cliente2]
print(clientes)

