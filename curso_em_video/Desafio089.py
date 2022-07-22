"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o
usuário possa mostrar as notas de cada aluno individualmente.
"""
aluno = list()
boletim = list()
while True:
    aluno.append(str(input('NOME: ')).strip().upper())
    aluno.append(float(input('NOTA 01: ')))
    aluno.append(float(input('NOTA 02: ')))
    boletim.append(aluno[:])
    aluno.clear()
    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if fim == 'N':
        break
print('=-' * 30)
for i, a in enumerate(boletim):
    print(f'O aluno {i + 1} - {boletim[i][0]} teve média {(a[1] + a[2]) / 2} ')
rev = str(input('Deseja rever as notas de algum aluno? ')).strip().upper()
if rev == 'NÃO':
    print('Obrigado')
for c in range(0, len(boletim)):
    if boletim[c][0] == rev:
        print(f'As notas do {boletim[c][0]} foram:\n'
              f'N1 - {boletim[c][1]}\n'
              f'N2 - {boletim[c][2]}')
