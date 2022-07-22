"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('=-=' * 30)
print(f'{"ESSE CAIXA TEM CÉDULAS DE R$50, R$20, R$10 E R$1":^85}')
print('=-=' * 30)

n50 = n20 = n10 = n1 = 0

valor = int(input('Qual o valor que deseja sacar? '))

n50 = valor // 50
n20 = (valor - (n50 * 50)) // 20
n10 = (valor - (n50 * 50 + n20 * 20)) // 10
n1 = valor - (n50 * 50 + n20 * 20 + n10 * 10)

print(f'Para sacar R${valor}, você receberá:\n'
      f' {n50} de R$50\n'
      f' {n20} de R$20\n'
      f' {n10} de R$10\n'
      f' {n1}  de R$1')
