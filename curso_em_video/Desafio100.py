"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint


def sorteio(a):
    for c in range(0, 5):
        a.append(randint(1, 10))
    print('=-' * 30)
    print(f'Foram sorteados os seguintes elementos: {a}')
    somaPar(a)


def somaPar(b):
    soma = 0
    for elementos in b:
        if elementos % 2 == 0:
            soma += elementos
    print('=-' * 30)
    print(f'A soma dos elementos pares é: {soma}')


numeros = list()
sorteio(numeros)
print('~' * 50)
