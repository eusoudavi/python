"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
from time import sleep

print(f'{" Desafio 51 ":=^50}')

a1 = int(input('Digite o valor do primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))

print('CALCULANDO', end='')
for a in range(1, 4):
    print('.', end='')
    sleep(.2)
print('')

for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, end=' -> ')
print('FIM')
