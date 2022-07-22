from datetime import date

ano = int(input('Digite um ano. Se você digitar 0, estará selecionando o ano atual: '))

if ano == 0:
    ano = date.today().year
bis = ano % 4

if bis == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano de {ano} não é Bissexto!')
