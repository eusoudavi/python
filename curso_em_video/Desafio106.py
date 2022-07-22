"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
from random import randint

while True:
    cor_aleatória = randint(41, 47)
    print('\033[1;' + f'{cor_aleatória}' + 'm')
    print('=' * 60)
    print(f'{"SISTEMA DE AJUDA - Python":^60}')
    print('=' * 60)
    print('\033[m')

    ajuda = str(input('Digite um comando que deseje ajuda: '))

    print('\033[7;40m')

    help(ajuda)
    print('\033[m')

    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if fim == 'N':
        break
    else:
        cor_aleatória = (randint(41, 47))
