"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
coisas = ('Arvore', 'Biblia', 'Regua', 'Computador', 'Lampada',
            'Cama', 'Casa', 'Roupa', 'Brinquedo')
for palavra in coisas:
    print('=-=' * 25)
    print(f'A palavra {palavra.upper()} tem as seguintes vogais:')
    for letras in range(0, len(palavra)):
        if palavra[letras] in 'aAeEiIoOuU':
            print(f'{palavra[letras].upper()} na posição {letras}')
