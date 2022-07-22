"""
 Melhore o DESAFIO 61,
 perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
from time import sleep

print(f'{" Desafio 61 ":=^50}')

a1 = int(input('Digite o valor do primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
n = 1
soma = a1
termos = int(input('Quantos termos você deseja verficar nessa PA? '))

print('CALCULANDO', end='')
for a in range(1, 4):
    print('.', end='')
    sleep(.2)
print('')

while n <= termos:
    if n < termos:
        print('{} -> ' .format(a1 + (n-1) * r), end='')
        n += 1
        soma += a1 + (n-1) * r
    if n == termos:
        print('{}'.format(a1 + (n - 1) * r))
        n += 1
        acrescimo = int(input('Deseja verificar mais quantos termos? '))
        if acrescimo > 0:
            soma += a1 + (n - 1) * r
        termos += acrescimo

print('Foram calculados {} termos e a soma de todos eles é {}' .format(termos, soma))
print('Fim')
