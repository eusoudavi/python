"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
import datetime

cadastro = {'NOME': str(input('NOME: ')).strip().capitalize(),
            'IDADE': int(input('ANO DE NASCIMENTO: ')),
            'CTPS': int(input('Nº CTPS: '))}
cadastro['IDADE'] = datetime.datetime.now().year - cadastro['IDADE']
if cadastro['CTPS'] != 0:
    cadastro['ADMISSÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    trabalhado = datetime.datetime.now().year - cadastro['ADMISSÃO']
    cadastro['SALÁRIO'] = float(input('SALÁRIO INICIAL: '))
    if trabalhado <= 35:
        cadastro['FALTA PARA APOSENTAR'] = 35 - trabalhado
print('=' * 40)
print(f'{"FICHA CADASTRADA":^40}')
print('=' * 40)
for k, v in cadastro.items():
    print(f'{k:.<30}{v:>10}')
