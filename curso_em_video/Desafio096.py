"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def terreno(l, c):
    area = l * c
    txt = f'A área do terreo de {l}m de largura com {c}m de comprimento é {area:.2f}m²'
    print('=' * (len(txt) + 2))
    print(f'{txt}')


larg = float(input('Qual a largura do terreo [m]? '))
comp = float(input('Qual o comprimento do terreo [m]? '))
terreno(larg, comp)
