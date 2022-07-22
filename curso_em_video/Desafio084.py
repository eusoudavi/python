"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
        A) Quantas pessoas foram cadastradas.
            B) Uma listagem com as pessoas mais pesadas.
                C) Uma listagem com as pessoas mais leves.
"""
cad = []
info = []
pesado = leve = 0
while True:
    cad.append(str(input('Digite o nome de uma pessoa: ')).strip().upper())
    # peso = float(input('Qual o peso da pessoa? '))
    cad.append(float(input('Qual o peso da pessoa? ')))
    info.append(cad[:])
    if len(info) == 1:
        pesado = leve = info[0][1]
    elif cad[1] > pesado:
        pesado = cad[1]
    elif cad[1] < leve:
        leve = cad[1]
    cad.clear()
    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if fim == 'N':
        break
print('=-' * 30)
print(f'Foram cadastradas {len(info)} pessoas')
print(f'O maior peso cadastrado é {pesado:.2f}Kg e o mais leve é {leve:.2f}Kg')
print('=-' * 30)
print('A lista das pessoas mais pesadas é:')
for c in sorted(info):
    if c[1] == pesado:
        print(f'{c[0]}')
print('=-' * 30)
print('A lista das pessoas mais leves é:')
for c in sorted(info):
    if c[1] == leve:
        print(f'{c[0]}')
