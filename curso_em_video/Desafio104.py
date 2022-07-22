"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaInt(txt=''):
    """
    FUNÇÃO PARA VALIDAÇÃO DE NÚMEROS INTEIROS

    :param txt: Opcional - Texto
    :return: Número inteiro
    """
    a = str(input(txt)).strip()
    while True:
        if a.isnumeric():
            return int(a)
        else:
            a = str(input('Digite um \033[31mNÚMERO\033[m inteiro '))


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
