"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
        B) A média de idade
            C) Uma lista com as mulheres
                D) Uma lista de pessoas com idade acima da média
"""
cads = []
med = med_mez = 0
pessoa = {}
while True:
    pessoa['nome'] = str(input('NOME: ')).strip().upper()
    pessoa['sexo'] = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if pessoa['sexo'] not in 'MF':
        while pessoa['sexo'] not in 'MF':
            pessoa['sexo'] = str(input('SEXO \033[31m[M/F]\033[m: ')).strip().upper()[0]
    pessoa['idade'] = int(input('IDADE: '))
    cads.append(pessoa.copy())
    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja continuar - \033[31mDIGITE APENAS SIM OU NÃO [S/N]?\033[m ')).strip().upper()[0]
    if fim in 'N':
        break
print(cads)
print('=' * 60)
print(f'Foram cadastradas {len(cads)} pessoas')
for i in cads:
    med += i['idade']
med = med // len(cads)
if med % len(cads) < 0:
    med_mez = (med % len(cads)) * 12
else:
    med_mez = 0
print(f'A média de idades cadastradas é {med} anos e {med_mez} meses' if med_mez > 0 else
      f'A média de idades cadastradas é {med} anos')
print('=' * 60)
print('Foram cadastradas as seguintes mulheres:')
for fem in cads:
    if fem['sexo'] in 'F':
        print(fem['nome'])
print('=' * 60)
print('A lista das pessoas acima da média de idade é:')
for acima in cads:
    if acima['idade'] > med:
        if acima['sexo'] in 'F':
            print(f'A {acima["nome"]} tem {acima["idade"]} de idade')
        else:
            print(f'O {acima["nome"]} tem {acima["idade"]} de idade')
print('=' * 60)
