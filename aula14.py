# TUDO EM PYTHON É UM OBJETO

a = 'AAAAA'
b = 'BBBBB'
c = 1.1

string = 'a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))