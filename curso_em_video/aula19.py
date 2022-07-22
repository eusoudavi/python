"""
DICIONÁRIO - {}
comando append não funciona
"""
# OPÇÃO 01
dado = dict()
# OPÇÃO 02
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
# PARA ACRESCENTAR UM ELEMENTO É:
dados['sexo'] = 'M'
# PARA APAGAR UM ELEMENTO:
del dados['idade']
print(dados)
print('=-' * 30)

filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}
"""
IMPORTANTE SABER A DIFERENÇA ENTRE VALOR CHAVE E ÍTEM
"""
print(filme.values())  # MOSTRA APENAS OS VALORES QUE CORRESPONDEM A CADA ÍNDICE
print(filme.keys())    # MOSTRA OS NOMES CADASTRADOS PARA CADA ÍNDICE
print(filme.items())   # MOSTRA TANTO OS VALORES COMO AS KEYS

print('=-' * 30)
for k, v in filme.items():
    print(f'O {k} é {v}')
"""
POSSO TER UMA LISTA COM VÁRIOS DISCIONÁRIOS DENTRO DELA
"""

"""
estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Feredativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())   # DIFERENTE DA CÓPIA DAS LISTAS, EM DISCIONÁRIO TEM O COMANDO COPY
    # NÃO PRECISA FICAR APAGANDO OS VALORES DA LISTA
print(brasil)
"""


"""
MÉTODO DE ORDENAÇÃO DE DICIONÁRIOS
"""
from random import randint
jogadores = dict()
jogadores['JOGADOR_01'] = randint(1, 6)
jogadores['JOGADOR_02'] = randint(1, 6)
jogadores['JOGADOR_03'] = randint(1, 6)
jogadores['JOGADOR_04'] = randint(1, 6)
print('=' * 30)
print(F'{"RESULTADO":^30}')
print('=' * 30)
ranking = sorted(jogadores, key=jogadores.get)  # LISTA
print(ranking)
for k in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'O {k} tirou {jogadores[k]}')
