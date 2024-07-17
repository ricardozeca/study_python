"""
Introdução ao try/excecpt
try -> tentar executar o código 
except -> occoreu algum erro ao tentar executar o código
"""
numero_str = input(
    'Vou dobrar o número que voce digitar: '
)
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
    
except:
    print('Isso não é um número')
# if numero_str.isdigit():    
# else:
#     