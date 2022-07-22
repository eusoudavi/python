"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
cont = ('zero', 'um', 'dois', 'trâs', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
teclado = int(input('Digite um número de zero à vinte: '))
if not 0 <= teclado <= 20:
    while teclado not in range(0,21):
        teclado = int(input('Digite um valor válido entre ZERO e VINTE! '))
print('*' * 50)
print(f'O número {teclado} escrito por extenso fica {cont[teclado].upper()}')
