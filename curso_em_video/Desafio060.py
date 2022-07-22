"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

num = int(input('Digite um valor inteiro: '))
a = num
fact = num
print('O fatorial de {}! é {}' .format(fact, num),end=' ')
while num != 1:
    num = num - 1
    print('x {}'.format(num),end=' ')
    fact = fact * num
print('= {}' .format(fact))
