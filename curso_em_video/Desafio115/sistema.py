from Desafio115.interface import *
from Desafio115.arquivo import  *

arq = 'desafio115.txt'
TesteArq(arq)

fim = True
while fim:
    op = iniciar(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'], 'Qual opção você deseja? ')
    if op == 1:
        fim = Op1('OPÇÃO 01')
        EscreverArq(arq)
    elif op == 2:
        fim = Op2('OPÇÃO 02 - PESSOAS CADASTRADAS')
        LerArq(arq)
    elif op == 3:
        fim = Op3('OPÇÃO 03')
