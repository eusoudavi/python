"""
 Desenvolva um programa que leia seis números inteiros
 e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o.
"""
print('{:=^50}' .format(' Desafio 50 '))

par = 0
imp = 0

for x in range(1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        par += num
    else:
        imp += num

print('A soma dos números pares que você digitou é: {}' .format(par))
print('A soma dos números ímpares que você digitou é: {}' .format(imp))
