"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime
from time import sleep

ano = int(input('Em que ano você nasceu? '))
atual = datetime.date.today().year

idade = atual - ano
print('Calculando...')
sleep(1)

if idade < 18:
    falta = 18 - idade
    print('Você tem {} anos e faltam {} anos para você se alistar no serviço militar' .format(idade, falta))
elif idade == 18:
    print('Você tem 18 anos e precisa se alistar neste ano ainda!')
else:
    passou = idade - 18
    print('Você tem {} anos e já passou {} anos do tempo que deveria ter se alistado.' .format(idade, passou))
