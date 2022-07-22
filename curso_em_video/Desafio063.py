"""
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""
print('=-=' *30)
print('Os 3 primeiros termos da sequência de Fibonacci são: 0 - 1 - 1')
print('=-=' *30)
n = int(input('Quantos termos a mais você deseja calcular da sequencia de Fibonacci? '))
f1 = 1
f2 = 1
cont = 0
print('A sequencia de Fibonacci para {} termos é: 0 - 1 - 1 - ' .format(n + 3), end='')
while cont <= n:
    fn = f2 + f1
    f1 = f2
    f2 = fn
    cont += 1
    if cont < n:
        print(f'{fn} - ' ,end='')
    elif cont == n:
        print(f'{fn}')
