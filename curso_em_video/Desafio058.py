"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

import random
from time import sleep
tentativas = 0
comp = random.randint(0, 10)
# SE QUISER DEIXAR O JOGO MAIS DIFÍCIL, REPETIR A RANDOMIZAÇÃO DENTRO DO WHILE
usuario = -1

print('Estou pensado em um número entre 0 e 10. \n')
while comp != usuario:
    usuario = int(input('Qual foi o número que eu pensei? '))
    tentativas += 1
    print('COMPARANDO...')
    sleep(.5)
    if comp is not usuario:
        print('Tente novamente!')

print('\nPARABÉNS, você acertou em {} tentativas' .format(tentativas))