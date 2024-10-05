
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Solicita ao usuário para digitar um número
entrada = input("Digite um número inteiro: ")

# # Verifica se a entrada é um número inteiro
try:
    numero = int(entrada)
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Não é um número inteiro.")

    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Solicita ao usuário para digitar a hora
# hora = input("Que horas são? ")

# Verifica se a entrada é um número inteiro e está no intervalo correto
# try:
#     hora = int(hora)
#     if 0 <= hora <= 23:
#         if 0 <= hora <= 11:
#             print("Bom dia")
#         elif 12 <= hora <= 17:
#             print("Boa tarde")
#         else:
#             print("Boa noite")
#     else:
#         print("Por favor, insira uma hora válida entre 0 e 23.")
# except ValueError:
#     print("Por favor, insira um número inteiro válido.")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# nome = str(input('Digite seu primeiro nome: '))

# tamanho_nome = len(nome)

# if tamanho_nome  <= 4:
#     print('Seu nome é curto')
# elif 5 <= tamanho_nome <= 6:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é muito grande')