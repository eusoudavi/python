"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
cads = []
while True:
    jogador = {'NOME': str(input('NOME: ')).strip().capitalize(),
               'NÚMERO DE PARTIDAS': int(input('Nº DE PARTIDAS: '))}
    gols = []
    for cont in range(1, jogador['NÚMERO DE PARTIDAS'] + 1):
        gols.append(int(input(f'Quantos gols {jogador["NOME"]} fez na {cont}º partida? ')))
    jogador['GOLS'] = gols[:]
    jogador['GOLS NO CAMPEONADO'] = sum(gols)
    cads.append(jogador.copy())
    jogador.clear()
    gols.clear()
    fim = str(input('Deseja encerrar o cadastro [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja encerrar o cadastro \033[31m[S/N]\033[m? ')).strip().upper()[0]
    if fim == 'S':
        break

print('=' * 60)
print(cads)
print('=' * 60)

print(f'{"RESULTADO":^60}')
print('=' * 60)
for d in cads:
    print(f'O jogador \033[34m{d["NOME"]}\033[m jogou {d["NÚMERO DE PARTIDAS"]} partidas e fez '
          f'{d["GOLS NO CAMPEONADO"]} gols no campeonato')
    for part, g in enumerate(d['GOLS']):
        print(f'    Na partida {part + 1} ele marcou {g} gols')
    print(f'O aproveitamento do {d["NOME"]} foi de {d["GOLS NO CAMPEONADO"] / d["NÚMERO DE PARTIDAS"]:.2f} gols/partida')
    print('=' * 60)