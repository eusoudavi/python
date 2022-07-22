"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
leitura = []
par = []
imp = []
while True:
    leitura.append(int(input('Digite um número inteiro: ')))
    fim = str(input('Deseja encerrar [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja encerrar [S/N]? ')).strip().upper()[0]
    if fim == 'N':
        break

for num in leitura:
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
print('=-' * 30)
print(f'Os valores coletados foram: {leitura}')
print(f'A lista com os valores pares é: {par}')
print(f'A lista com os valores ímpares é: {imp}')
print('=-' * 30)
