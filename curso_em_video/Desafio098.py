"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
"""
from time import sleep


def contador(a1, an, passo):
    global x
    if passo == 0:
        passo = 1
    print(f'Contando de {a1} até {an} de {passo} em {passo}:')
    if a1 > an and passo > 0:
        passo = passo * (-1)
    for x in range(a1, an, passo):
        print(f'{x} ', end='')
        sleep(.2)
    if x + passo <= an and passo > 0:
        print(an)
    elif x + passo >= an and passo < 0:
        print(an)


print('=-' * 30)
contador(0, 10, 1)
print('=-' * 30)
contador(10, 0, -2)
print('=-' * 30)

a1 = int(input('Digite o valor inicial da contagem: '))
an = int(input('Digite o valor final da contagem: '))
passo = int(input('Qual o passo da contagem: '))

contador(a1, an, passo)

