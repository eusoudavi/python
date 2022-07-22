"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""
num = (int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')),
       int(input('Digite um terceiro número inteiro: ')),
       int(input('Digite o quarto número inteiro: ')))
print('=-' * 30)
print(f'Você digitou os seguintes números: {num}')

print('=-' * 30)

if num.count(9) != 0:
    print(f'O número 9 apareceu {num.count(9)} vez' if num.count(9) == 1 else
          f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não apareceu')

print('=-' * 30)

if num.count(3) != 0:
    print(f'O número 3 apareceu na posição {num.index(3)}', end='')
    if num.count(3) > 1:
        for n in range(1, num.count(3)):
            if n == (num.count(3) - 1):
                print(f' e {num.index(3, num.index(3) + n)}')
            else:
                print(f', {num.index(3, num.index(3) + n)}', end='')
    elif num.count(3) == 1:
        print('')
else:
    print('O número 3 não apareceu')

print('=-' * 30)

for a, b in enumerate(num):
    if b % 2 == 0 and b != 0:
        print(f'O número {b} na posição {a} é PAR')
