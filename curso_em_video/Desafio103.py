"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
"""


def ficha(n='', g=0):
    print(f'O jogador {n} marcou {g} gols no campeonato.')


print('=-' * 30)
n = str(input('Digite o nome do Jogador: ')).strip()
if n in '':
    n = 'DESCONHECIDO'
g = str(input('Quantos gols ele marcou? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
print(ficha(n, g))
