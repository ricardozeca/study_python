# nome = str( input ('Digite seu nome:'))
# idade = int( input ('Digite sua idade:'))
# peso = float( input ('Digite seu peso:'))

# print(f'Seu nome é {nome}')
# print(f'Sua idade é {idade}')
# print(f'Seu peso é {peso}')

# soma = 1 + 1
# multiplicacao = 4 * 4
# divisao = 30 / 3
# potencia = 7 ** 2

# print('soma', soma)
# print('multiplicacao', multiplicacao)
# print('divisao', divisao)
# print('potencia', potencia)

# idade = int(input ('Informe sua idade:'))

# if idade >= 18:
#     print('PERMITIDO')
# else:
#     print('NÃO PERMITIDO')

# salario = float(input('Informe o salário: '))

# if salario <= 3000:
#     print('Programador Júnior')
# elif salario > 3000 and salario <=6000:
#     print('Programador Pleno')
# elif salario > 6000 and salario <= 15000:
#     print('Programador Sênior')
# else:
#     print('Gerente de projetos')

# lista_numeros = [1, 2, 3]

# lista_numeros[0] = 27

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# lista_vazia = []

# lista_vazia.append('Hello')
# lista_vazia.append('World')

# print(lista_vazia)

# numeros = [10, 9, 8, 7, 6]

# print ('total:', len(numeros)) # Total de itens da lista
# print('menor valor:', min(numeros)) # Menor valor da lista
# print('maior valor:', max(numeros)) # maior valor da lista

# notas = []

# for x in range(5):
#     codigo_aluno = input('RM: ')
#     nota = float(input('Nota: '))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

# print ('quantidade de notas:', len(notas))

# for n in notas:
#     codigo_aluno = n[0]
#     nota = n[1]
#     print('O RM', codigo_aluno, 'tirou a nota:', nota)

# notas = []

# contador = 1

# while contador <= 5:
#     codigo_aluno = input('RM: ')
#     nota = float(input('Nota: '))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)
#     contador = contador + 1

# print ('qunatidade de notas inseridas', len(notas))


# pessoa = {
#     'nome': 'Ricardo Lindão',
#     'idade': 27,
#     'peso': 56.2
# }

# print(pessoa['nome'])
# print(pessoa['idade'])
# print(pessoa['peso'])

def minha_funcao (valor1, valor2):
    return valor1 + valor2

while True:
    valor1 =int(input('Valor1: '))
    valor2 =int(input('Valor2: '))

    resposta = minha_funcao(valor1, valor2)

    print(valor1, '+', valor2, '=', resposta )

    break
