"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = {}
boletim = []
while True:
    aluno['nome'] = str(input('Qual o nome do aluno? ')).strip().capitalize()
    aluno['média'] = float(input('Qual a média do aluno? '))
    if 10.0 >= aluno['média'] >= 7.0:
        aluno['situação'] = 'APROVADO'
    elif 7.0 > aluno['média'] > 5.0:
        aluno['situação'] = 'RECUPERAÇÃO'
    else:
        aluno['situação'] = 'REPROVADO'
    boletim.append(aluno.copy())
    fim = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if fim in 'N':
        break
print('=' * 60)
print(f'{"BOLETIM":^60}')
print('=' * 60)
print(f'{"NOME:":<20}' f'{"MÉDIA:":^20}' f'{"SITUAÇÃO:":>20}')
print('_' * 60)
for c in boletim:
    print(f'{c["nome"]:_<20}{c["média"]:_^20.2f}{c["situação"]:_>20}')
