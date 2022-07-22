"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
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


def leiaFloat(txt=''):
    while True:
        try:
            a = float(input(txt))
        except (ValueError, TypeError):
            print(f'Valor inválido')
            continue
        except KeyboardInterrupt:
            print('Programa encerrado de forma inesperada!')
        else:
            return float(a)


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
m = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o número rela {m}')