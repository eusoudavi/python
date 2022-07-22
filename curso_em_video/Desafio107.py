"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda

VALOR = float(input('Digite um valor: '))
AUMENTO = int(input('Em quantos porcentos deseja aumentar? '))
DIMINUIR = int(input('Em quantos porcentos deseja diminuir? '))
print('=-' * 30)

print(f'O valor digitado foi R${VALOR:.2f} e aumentando {AUMENTO}% temos R${moeda.aumentar(VALOR, AUMENTO):.2f}')
print(f'O valor digitado foi R${VALOR:.2f} e diminuir {DIMINUIR}% temos R${moeda.diminuir(VALOR, DIMINUIR):.2f}')
print(f'O dobro de R${VALOR:.2f} é R${moeda.dobro(VALOR):.2f}')
print(f'A metade de R${VALOR:.2f} é R${(moeda.metade(VALOR)):.2f}')
