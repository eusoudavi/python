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