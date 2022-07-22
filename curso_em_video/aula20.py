"""
Nessa aula, vamos aprender o que são FUNÇÕES ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de
nossos códigos em Python. Veja como funciona o comando def em Python e como
utilizá-lo com parâmetros simples e múltiplos.

FUNÇÃO -> ROTINA
"""


def mostralinha():
    print('=' * 60)


# PROGRAMA PRINCIPAL - DEIXAR DUAS LINHAS ENTRE A FUNÇÃO E O PROGRAMA PRINCIPAL
mostralinha()
print(f'{"FUNÇÕES":^60}')
mostralinha()


# PODEMOS USAR A FUNÇÃO COM UM PARÂMETRO
def mensagem(msg):
    print('=' * 60)
    print(f'{msg:^60}')
    print('=' * 60)


mensagem('PARÂMETRO')


# EMPACOTAMENTO!
# PODEMOS COLOCAR QUANTOS VALORES QUISERMOS EM UM PARÂMETRO
def contador(num):
    s = 0
    for valores in num:
        s += valores
    print(f'Somando os valores {num} temos {s}')


contador(1, 2)
contador(5, 10, 15, 20)
