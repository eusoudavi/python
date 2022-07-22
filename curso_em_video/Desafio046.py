"""
Faça um programa que mostre na tela uma
contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
"""
from time import sleep

print('{:_^50}'.format('CONTAGEM REGRESSIVA!!!'))
print('PREPARANDO A CONTAGEM', end='')
for c in range(0,3):
    sleep(.35)
    print('.',end='')

print('')
for a in range(10, -1, -1):
    print(a)
    sleep(1)
