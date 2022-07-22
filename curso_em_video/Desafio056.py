"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
print(f'{" Desafio 56 ":=^50}')
soma_idades = 0
velho = 0
mulheres_novas = 0

for i in range(1,5):
    n = str(input('Qual o nome da {}ª pessoa? ' .format(i)))
    print('Qual o sexo da pessoa? \n'
          '[ M ] MASCULINO \n'
          '[ F ] FEMININO ')
    s = str(input(' '))
    if s == 'M':
        id = int(input('Qual a idade do {}? '.format(n)))
        if id > velho:
            velho = id
            nome_velho = n
    elif s == 'F':
        id = int(input('Qual a idade da {}? ' .format(n)))
        if id < 20:
            mulheres_novas += 1
    else:
        print('Escolha entre M e F')
    soma_idades += id

média = soma_idades / 4
print('A média de idades das 4 pessoas é {} anos. \n'
      'O homem mais velho é o {} e tem {} anos \n'
      'No grupo tem {} mulher(es) com menos de 20 anos' .format(média, nome_velho, velho, mulheres_novas))
