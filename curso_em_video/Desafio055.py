"""
 Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
pessoa_maior = 0
menor = 0
pessoa_menor = 0

for n in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            pessoa_maior = n
        if peso < menor:
            menor = peso
            pessoa_menor = n

print('\nDas pessoas analisadas, a {}ª pessoa tem o maior peso que é {:.1f}Kg.\n'
      'A {}ª pessoa tem o menor peso que é {:.1f}Kg.' .format(pessoa_maior, maior, pessoa_menor, menor))
