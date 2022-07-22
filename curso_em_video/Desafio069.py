"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

maior = hom = mul = 0
while True:
    idade = int(input('Qual a idade da pessoa? '))
    if idade >= 18:
        maior += 1

    sex = str(input('Qual o sexo da pessoa [M/F]? ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Qual o sexo da pessoa [M/F]? ')).strip().upper()[0]

    if sex == 'M':
        hom += 1
    if sex == 'F' and idade >= 20:
        mul += 1
    print('Cadastro Efetivado')
    print('=-' * 30)
    continuar = str(input('Deseja continuar [S/N]:')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]:')).strip().upper()
    if continuar == 'N':
        break
print('='* 60)
print(f'Ao todo foram cadastradas {maior} maiores de 18 anos!\n'
      f'Foram {hom} homens cadastrados.\n'
      f'Foram {mul} mulheres com mais de 20 anos cadastradas.')