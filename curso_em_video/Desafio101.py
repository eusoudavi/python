"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano=2021):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Você tem {idade} anos e ainda \033[31mnão pode votar'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos e seu voto é \033[33mopcional'
    else:
        return f'Você tem {idade} anos e seu voto é \033[32mobrigatório'


a = int(input('Qual o seu ano de nascimento? '))
print(voto(a))
