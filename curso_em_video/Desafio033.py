"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
from time import sleep

a = int(input('Digite um número inteiro: '))
b = int(input('Mais um: '))
c = int(input('E mais um: '))
print('ANALISANDO AS INFORMAÇÕES...')
sleep(1)

if a > b and a > c:
    print(f'O maior número é {a}')
    if b > c:
        print(f'O segundo maior número é {b}')
        print(f'O menor número é o {c}')
    else:
        print(f'O segundo maior número é o {c}')
        print(f'O menor número é o {b}')
else:
    if b > c:
        print(f'O maior número é o {b}')
        if c > a:
            print(f'O segundo maior número é o {c}')
            print(f'O menor número é o {a}')
        else:
            print(f'O segundo maior número é o {a}')
            print(f'O menor número é o {c}')
    else:
        print(f'O maior número é o {c}')
        if b > a:
            print(f'O segundo maior número é o {b}')
            print(f'O menor número é o {a}')
        else:
            print(f'O segundo menor número é o {a}')
            print(f'O menor número é o {b}')
