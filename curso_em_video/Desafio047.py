"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

from time import sleep

print('{:=^50}' .format(' DESAFIO 47 '))
print('Entre 1 e 50 temos os seguintes números pares:')
for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.1)
