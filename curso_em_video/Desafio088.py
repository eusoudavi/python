"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
jogos = int(input('Quantos jogos deseja gerar? '))
num = 0
sorteio = []
total = []
for c in range(0, jogos):
    while len(sorteio) != 6:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
    sorteio.sort()
    total.append(sorteio[:])
    sorteio.clear()
print('=-' * 30)
for a in sorted(total):
    print(a)
    sleep(.5)