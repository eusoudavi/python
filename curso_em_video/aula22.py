"""
Módulos:
    Arquivos com funções úteis ao seu programa origianl

Pacotes (Bibliotecas):
    Quando os módulos ficam muito grandes, podemos distribuir os módulos em pacotes
    Python package
"""
# MÓDULOS
import funcoes_aula22
# PACOTES
from uteis import números

a = funcoes_aula22.leiaInt('Digite um número inteiro: ')
fat = funcoes_aula22.fatorial(a)    # ESTÁ CHAMANDO A FUNÇÃO DO MÓDULO
fat2 = números.fatorial(a)          # ESTÁ CHAMANDO A FUNÇÃO DO PACOTE
print(f'O fatorial de {a} é {fat}')
