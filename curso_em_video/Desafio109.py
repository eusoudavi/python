"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se
o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda

VALOR = float(input('Digite um valor: '))
AUMENTO = int(input('Em quantos porcentos deseja aumentar? '))
DIMINUIR = int(input('Em quantos porcentos deseja diminuir? '))
print('=-' * 30)

print(f'O valor digitado foi {moeda.converte(VALOR)} e aumentando {AUMENTO}% temos '
      f'{moeda.aumentar(VALOR, AUMENTO, True)}')
print(f'O valor digitado foi {moeda.converte(VALOR)} e diminuir {DIMINUIR}% temos '
      f'{moeda.diminuir(VALOR, DIMINUIR, True)}')
print(f'O dobro de {moeda.converte(VALOR)} é {moeda.dobro(VALOR, True)}')
print(f'A metade de {moeda.converte(VALOR)} é {moeda.metade(VALOR, True)}')