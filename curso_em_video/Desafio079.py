"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
val = []
while True:
    leitor = int(input('Digite um valor: '))
    if leitor not in val:
        val.append(leitor)
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
val.sort()
print('=-' * 30)
print(f'Os valores digitados foram: {val[0]} ', end='')
for index, valor in enumerate(val):
    if index == len(val) - 1 and index != 0:
        print(f'e {valor}')
    elif index != 0:
        print(f', {valor} ', end='')

