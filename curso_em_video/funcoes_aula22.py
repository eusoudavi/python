def fatorial(num):
    """
    PROGRAMA PARA CALCULO DE FATORIAL
    :param num: NÚMERO QUE SERÁ CALCULADO O FATORIAL
    :return: FATORIAL
    """
    fac = 1
    for c in range(1, num + 1):
        fac *= c
    return fac


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
