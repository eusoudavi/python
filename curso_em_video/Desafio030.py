"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
n = int(input('Digite um número: '))

par = n % 2
if par == 0:
    print('O número {} é um número PAR!' .format(n))
else:
    print('O número {} é um número IMPAR' .format(n))
