"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""
times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino',
         'Fortaleza', 'Corinthians', 'Internacional', 'Fluminense',
         'América-MG', 'Cuiabá', 'Atlético-GO', 'São Paulo', 'Ceará',
         'Athletico-PR', 'Santos', 'Bahia', 'Sport', 'Juventude',
         'Grêmio', 'Chapecoense')

print('=-=' * 60)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('=-=' * 60)
print(f'Os quatro últimos classificados são {times[-4:]}')
print('=-=' * 60)
print('A lista de times do Campeonato Brasileiro em ordem alfabética é:')
for t in sorted(times):
    print(t)
print('=-=' * 60)
print(f'O time da Chapeconense está em {times.index("Chapecoense") + 1}º posição')
print('=-=' * 60)
print('A classificação total do campeonato brasileiro é:')
for a, b in enumerate(times):
    print(f'{a + 1:<2} - {b}')
