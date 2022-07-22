"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
"""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um segundo número inteiro: '))

if n1 > n2:
    print('O número {} é maior que {}' .format(n1, n2))
elif n1 < n2:
    print('O número {} é maior que {}' .format(n2, n1))
else:
    print('Os número são iguais!')
