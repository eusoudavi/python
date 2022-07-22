"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random
import time

print('{:_^50}'.format(' GAME - JOKENPÔ '))
escolha = str(input('Escolha entre PEDRA, PAPEL OU TESOURA: ')).strip().lower()
print('JÔ', end=' ')
time.sleep(.5)
print('KEN', end=' ')
time.sleep(.6)
print('PÔ')
time.sleep(.7)

print('=-=' * 15)
computador = random.randint(0, 2)
# PEDRA = 1
# PAPEL = 2
# TESOURA = 3
op = ('Pedra', 'Papel', 'Tesoura')
print('Eu escolhi {}'.format(op[computador]))
"""
if computador == 1:
    print('Eu escolhi PEDRA\n')
elif computador == 2:
    print('Eu escolhi PAPEL\n')
else:
    print('Eu escolhi TESOURA\n')
"""
if (escolha == 'pedra' and computador == 0) or (escolha == 'papel' and computador == 1) or (escolha == 'tesoura'
                                                                                            and computador == 2):
    print('EMPATE')

if escolha == 'pedra':
    if computador == 1:
        print('\033[31mCOMPUTADOR GANHA \033[m')
    elif computador == 2:
        print('\033[34mUSUÁRIO GANHA \033[m')
elif escolha == 'papel':
    if computador == 2:
        print('\033[31mCOMPUTADOR GANHA \033[m')
    elif computador == 0:
        print('\033[34mUSUÁRIO GANHA \033[m')
else:
    if computador == 0:
        print('\033[31mCOMPUTADOR GANHA \033[m')
    elif computador == 1:
        print('\033[34mUSUÁRIO GANHA \033[m')
print('=-=' * 15)
