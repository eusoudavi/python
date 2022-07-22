"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {'NOME': str(input('NOME: ')).strip().capitalize(),
           'NÚMERO DE PARTIDAS': int(input('Nº DE PARTIDAS: '))}
gols = []
for cont in range(1, jogador['NÚMERO DE PARTIDAS'] + 1):
    gols.append(int(input(f'Quantos gols {jogador["NOME"]} fez na {cont}º partida? ')))
jogador['GOLS'] = gols[:]
jogador['GOLS NO CAMPEONADO'] = sum(gols)
print('=' * 60)
print(f'{"RESULTADO":^60}')
print('=' * 60)
print(jogador)
print('=' * 60)
for k, v in jogador.items():
    print(f'{k:.<50}{v}')
