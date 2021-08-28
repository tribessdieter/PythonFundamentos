# Curso : python Fundamentos proway
#  AULA : DIA 2- PARTE 3
# ASSUNTO : Listas, Tuplas, Dicionários
# DATA : 2021-08-28-m 'Aula2 - parte 2 - While'

bebidas = ['Coca-Cola','Skol','cachaça','Agua']
print(bebidas)
print(bebidas[1] )# segundo elemento da lista
print(bebidas[3] )# quarto elemento da lista
print(bebidas[1:] )# ate o final
print(bebidas[:3] )# do inicio ate o terceiro elemento da lista

bebidas.append("Corona")
print(bebidas)
bebidas[3] = "Vodka"
print(bebidas)
bebidas.remove('Skol')
print(bebidas)
bebidas.pop(-1)
print(bebidas)
ultima_bebida = bebidas.pop(-1)
print(ultima_bebida)
print(bebidas)
# inserir
bebidas.insert(0,'refri')
bebidas.insert(2,'café')
print(bebidas)
# deleta um dado ou intervalo de dados de uma lista
del(bebidas[1:3])
print(bebidas)

# CRUDE
# C - Create
# R - Read
# u - 