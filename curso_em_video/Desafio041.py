"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))

atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos e a categoria dele é:')

if idade < 9:
    print('MIRIM')
elif 9 <= idade < 14:
    print('INFANTIL')
elif 14 <= idade < 19:
    print('JUNIOR')
elif 19 <= idade < 25:
    print('SÊNIOR')
else:
    print('MASTER')
