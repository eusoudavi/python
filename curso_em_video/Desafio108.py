"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""
import moeda

VALOR = float(input('Digite um valor: '))
AUMENTO = int(input('Em quantos porcentos deseja aumentar? '))
DIMINUIR = int(input('Em quantos porcentos deseja diminuir? '))
print('=-' * 30)

print(f'O valor digitado foi {moeda.converte(VALOR)} e aumentando {AUMENTO}% temos '
      f'{moeda.converte(moeda.aumentar(VALOR, AUMENTO))}')
print(f'O valor digitado foi {moeda.converte(VALOR)} e diminuir {DIMINUIR}% temos '
      f'{moeda.converte(moeda.diminuir(VALOR, DIMINUIR))}')
print(f'O dobro de {moeda.converte(VALOR)} é {moeda.converte(moeda.dobro(VALOR))}')
print(f'A metade de {moeda.converte(VALOR)} é {moeda.converte(moeda.metade(VALOR))}')
