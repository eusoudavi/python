"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
km = float(input('Quantos quilômetros tem a sua viagem? '))

if km <= 200:
    preco = km * 0.50
    print('Você vai pagar R$ 0,50 por quilômeto.')
    print('O preço da passagem é de R${:.2f}' .format(preco))
else:
    preco = km * 0.45
    print('Você vai pagar R$ 0,45 por quilômeto.')
    print('O valor da passagem é de R${:.2f}' .format(preco))
