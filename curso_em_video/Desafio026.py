"""
Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez
e em que posição ela aparece a última vez.
"""
frase = str(input('Escreva uma frase qualquer: ')).strip().lower()
prim = frase.count('a')
inv = frase[::-1]
ult = len(inv) - inv.find('a')
print('...')
print('A frase digitada possui {} caracteres.'.format(len(frase)))
print('')

if prim == 1:
    print('A letra "a" aparece {} vezes na frase que você digitou na posição {}' .format(prim, frase.find('a')+1))
    # poderia ultizar o comando frase.rfind('a')
else:
    if prim > 1:
        print('A letra "a" aparece {} vezes na frase que você digitou. \n'
              'A primeira vez que ela aparece é na posição {}. \n'
              'A última vez que ela aparece é na posição {}.'.format(prim, frase.find('a') + 1, ult))
        # poderia ultizar o comando frase.rfind('a')
    else:
        print('A frase digitada não possui a leta "a"')
