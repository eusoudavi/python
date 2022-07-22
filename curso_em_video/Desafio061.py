"""
Refaça o DESAFIO 51,
lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
from time import sleep

print(f'{" Desafio 61 ":=^50}')

a1 = int(input('Digite o valor do primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
n = 1

print('CALCULANDO', end='')
for a in range(1, 4):
    print('.', end='')
    sleep(.2)
print('')

while n < 11:
    print('{} -> ' .format(a1 + (n-1) * r), end='')
    n += 1
print('Fim')
