"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante.
"""

frase = str(input('Digite uma frase qualquer: ')).strip().lower()

lista = frase.split()
s_esp = ''.join(lista)
invertida = s_esp[::-1]

if invertida == s_esp:
    print('Sua frase é um POLÍNDROMO')
else:
    print('Sua frase não é um POLÍNDRONO')

# OUTRA FORMA COM O LAÇO:
print('')

inverso = ''
for l in range(len(s_esp) -1, -1, -1):
    inverso += s_esp[l]
print(inverso)

