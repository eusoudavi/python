"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
import datetime

print(f'{" Desafio 54 ":=^50}')

print('Neste programa vamos ler o ano de nascimento [xxxx] de 7 pessoas.\n'
      'Queremos saber quais delas ainda não atingiram a mior idade')
dados = []
ok = []
cont = 0
for n in range(1, 8):
    pessoa = int(input(f'Qual o ano de nascimento da pessoa {n}? '))
    dados.insert(n - 1, pessoa)
    if datetime.date.today().year - pessoa >= 18:
        print('Ela é maior de idade')
        cont += 1
        ok.insert(n - 1, 1)
    else:
        print('Ela é menor de idade')
        ok.insert(n - 1, 0)

print('Das pessoas que você informou, {} são maiores de idade.\n'
      'Assim temos as seguintes pessoas:' .format(cont))

for index, item in enumerate(ok):
    if item == 1:
        print('A pessoa {} nasceu em {} e possui {} anos.'.format(index + 1, dados[index],
                                                                  datetime.date.today().year - dados[index]))

# print(dados)
# print(ok)
