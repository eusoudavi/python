"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    tab = int(input('Quer ver a tabuáda de qual valor [DIGITE UM NÚMERO NEGATIVO PARA PARAR]: '))
    if tab < 0:
        break
    print(f'{"":=<20}{" A TABUADA DE ":^12}{tab :^2}{"":=>20}')
    for i in range(1, 11):
        print(f'{tab} x {i} = {tab * i}')
    print(f'{" FIM ":=^55}')
print('Programa encerrado')
