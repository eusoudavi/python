"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print(f'{" Desafio 52 ":=^50}')

num = int(input('Digite um valor inteiro: '))
cont = 0

for x in range(1, num + 1):
    if num % x == 0:
        if x == 1 or x == num:
            print('\033[34m', end='')
        else:
            print('\033[33m', end='')
        print('O número {} é divisível por {}'.format(num, x))
        cont += 1

if cont == 2:
    print('\n\033[32mO número {} é PRIMO'.format(num))
else:
    print('\n\033[31mO número {} NÃO É PRIMO'.format(num))
