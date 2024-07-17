"""
Exercício
Peça ao usuário para digitar seu nome OK
Peça ao usuário para digitar sua idade OK
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} OK
        Seu nome invertido é {nome invertido} OK
        Seu nome contém (ou não) espaços OK
        Seu nome tem {n} letras OK
        A primeira letra do seu nome é {letra} OK
        A última letra do seu nome é {letra} OK
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios." OK
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome NÃO contém espaços")

    print(f"Seu nome tem {len(nome)} letras") # AQUI E PARA VER QUANTAS LETRAS TEM USANDO LEN
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")
