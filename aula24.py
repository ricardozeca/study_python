# Operadores in e not in
# String  são iteráveis 
# 0 1 2 3 4 5
# R i c a r d o
# -6-5-4-3-2-1
# nome = 'Ricardo'
# print(nome[2])
# print(nome[-5])
# print('Ric' in nome)
# print('p' in nome)
# print( 10* '-')
# print('Ric' not in nome)
# print('p' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')