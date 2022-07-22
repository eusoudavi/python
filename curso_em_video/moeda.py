def aumentar(valor, inc=100, conv=False):
    """
    FUNÇÃO PARA AUMENTAR VALOR MONETÁRIO
    :param valor: VALOR FINANCEIRO
    :param inc: VALOR EM PORCENTAGEM
    :param conv: [OPCIONAL] CONVERTER UNIDADE PARA REAL E FORMATAR PARA O PADRÃO CORRESPONDENTE
    :return: VALOR ACRESCIDO DA PORCENTAGEM DE INCREMENTO

    By Davi M. Visintainer
    """
    aumento = inc * valor / 100
    resultado = valor + aumento
    return resultado if not conv else converte(resultado)


def diminuir(valor, dec=100, conv=False):
    diminui = dec * valor / 100
    resultado = valor - diminui
    return resultado if not conv else converte(resultado)


def dobro(valor, conv=False):
    valor *= 2
    return valor if not conv else converte(valor)


def metade(valor, conv=False):
    valor /= 2
    return valor if not conv else converte(valor)


def converte(valor, unidade='R$'):
    return f'{unidade} {valor:.2f}'.replace('.', ',')


def resumo(valor, aumenta=0, diminui=0, unidade='R$'):
    print('=' * 60)
    print(f'{"RESUMO DO VALOR":^60}')
    print('=' * 60)
    print(f'{"Preço Analisado":<25}{"." * 15}{converte(valor, unidade):>20}')
    if aumenta != 0:
        print(f'{aumenta:>3}{"% de aumento":<22}{"." * 15}{aumentar(valor, aumenta, True):>20}')
    if diminui != 0:
        print(f'{diminui:>3}{"% de redução":<22}{"." * 15}{diminuir(valor, diminui, True):>20}')
    print(f'{"O dobro de ":<1}{converte(valor, unidade):<14}{"." * 15}{dobro(valor, True):>20}')
    print(f'{"A metade de ":<1}{converte(valor, unidade):<13}{"." * 15}{metade(valor, True):>20}')
    print('=' * 60)
