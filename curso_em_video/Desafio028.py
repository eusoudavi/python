"""
Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
from time import sleep

comp = random.randint(0, 5)
print('Estou pensado em um número entre 0 e 5. \n')
usuario = int(input('Qual foi o número que eu pensei? '))

print('COMPARANDO...')
sleep(2)

if comp == usuario:
    print('PARABÉNS, você acertou')
else:
    print('VOCÊ ERROU, eu pensei no número {}. \n'
          'Tente novamente!' .format(comp))
