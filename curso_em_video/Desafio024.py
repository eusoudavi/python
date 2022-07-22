"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""
nome = str(input('Digite o de uma cidade: ')).strip().upper()
check = nome.find('SANTO')

if check >= 0:
    print('O nome da cidade contem a palavra SANTO')
else:
    print('O nome da cidade não contem a palavra SANTO')

print('SANTO' in nome)
