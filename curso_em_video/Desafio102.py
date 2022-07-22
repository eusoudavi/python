"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.
"""


def fatorial(num, show='N'):
    """
    PROGRAMA PARA CALCULO DE FATORIAL
    :param num: NÚMERO QUE SERÁ CALCULADO O FATORIAL
    :param show: MOSTRAR O PROCESSO DE CÁLCULO
    :return: FATORIAL
    """
    fac = 1
    for c in range(1, num + 1):
        fac *= c
        if show == 'S':
            if c != num:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return fac


a = int(input('Digite um número inteiro: '))
most = str(input('Deseja mostrar o cálculo [S/N]? ')).strip().upper()[0]

print(fatorial(a, most))
