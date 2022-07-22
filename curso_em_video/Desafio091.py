"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
import time
jogadores = dict()
jogadores['JOGADOR_01'] = randint(1, 6)
jogadores['JOGADOR_02'] = randint(1, 6)
jogadores['JOGADOR_03'] = randint(1, 6)
jogadores['JOGADOR_04'] = randint(1, 6)
print('=' * 30)
print(f'{"RESULTADO":^30}')
print('=' * 30)
for k in sorted(jogadores, key=jogadores.get, reverse=True):
    time.sleep(.8)
    print(f'O {k} tirou {jogadores[k]}')
