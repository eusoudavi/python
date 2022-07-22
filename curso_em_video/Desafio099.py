"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(n):
    high = 0
    for valores in n:
        if valores > high:
            high = valores
    print(f'Foram digitados {len(n)} valores.')
    print(f'O maior valor digitado foi: {high}')


armazenamento = []
while True:
    a = int(input('Digite um número: '))
    armazenamento.append(a)
    cont = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if cont == "N":
        break
print('=-' * 30)
maior(armazenamento)
