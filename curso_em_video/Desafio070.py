"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

from time import sleep
total = caro = 0
nome = str(input('Qual o nome do produto? ')).strip().upper()
preco = float(input('Qual o preço desse produto? '))
barato = preco
nome_barato = nome
while True:
    total += preco
    if preco >= 1000:
        caro += 1
    if preco < barato:
        nome = nome_barato
    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if fim == 'N':
        break
    nome = str(input('Qual o nome do produto? ')).strip().upper()
    preco = float(input('Qual o preço desse produto? '))
print('=-='*20)
print(f'{" FECHANDO A COMPRA! ":^50}')
sleep(.5)
print('=-='*20)
print(f'O total gasto foi de R${total:.2f}.\n')
print(f'No total {caro} custaram acima de R$1000.00\n' if caro > 0 else ''
      f'O produto mais barato é o(a) {nome_barato}.')
