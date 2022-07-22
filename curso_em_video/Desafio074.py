"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random

tupla = (random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5),
         random.randint(0, 5))
print(f'A tupla gerada foi: {tupla}')
print('=-' * 30)
print('Listando em ordem, temos:')
for pos, item in enumerate(tupla):
    if pos == 0:
        maior = menor = item
    elif item > maior:
        maior = item
    elif item < menor:
        menor = item
    print(f'{pos} - {item}')
print('=-' * 30)
print(f'O maior item dessa tupla foi {maior} e o menor foi {menor}')
# OPÇÃO MELHOR:
print(f'O maior item dessa tupla foi {max(tupla)} e o menor foi {min(tupla)}')
