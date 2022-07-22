"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
    Ex:
    escreva(‘Olá, Mundo!’)
    Saída:
    ~~~~~~~~~
    Olá, Mundo!
    ~~~~~~~~~
"""


# ALINHANDO NS ESQUERDA COM PREENCHIMENTO
def frase_esq(txt):
    print('=' * (len(txt) + 6))
    print(txt.ljust(len(txt) + 6, '_'))
    print('=' * (len(txt) + 6))


# ALINHANDO NO CENTRO SEM PREENCHIMENTO
def frase_cnt(txt):
    print('=' * (len(txt) + 6))
    print(txt.center(len(txt) + 6))
    print('=' * (len(txt) + 6))


# ALINHANDO NA DIREITA COM PREENCHIMENTO
def frase_dir(txt):
    print('~' * (len(txt) + 6))
    print(txt.rjust(len(txt) + 6, '.'))
    print('~' * (len(txt) + 6))


us = str(input('Digite a frase que será alinhada à esquerda: ')).strip()
frase_esq(us)
us = str(input('Digite a frase que será alinhada no centro: ')).strip()
frase_cnt(us)
us = str(input('Digite a frase que será alinhada à direita: ')).strip()
frase_dir(us)
