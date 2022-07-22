"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
name = str(input('Digite o nome de alguém: ')).strip().upper()
l = name.split()
check = l.index('SILVA')
number = len(l)

print('O nome que você escreveu contém {} palavras.'.format(number))

if check >= 0:
    print(F'O nome contém a palavra SILVA na posição {check + 1}')
else:
    print('O nome não contém a palavra Silva')
# print(check)
