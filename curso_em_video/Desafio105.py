"""
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
    – Quantidade de notas
    – A maior nota
    – A menor nota
    – A média da turma
    – A situação (opcional)
"""


def notas(* n, sit=False):
    """
    FUNÇÃO PARA AVALIAÇÃO DAS NOTAS DE VÁRIOS ALUNOS.

    :param n: NÚMERO INDETERMINADO DE NOTAS
    :param sit: OPICIONAL - VERIFICAR A SITUAÇÃO DA TURMA (BOOLEAN)
    :return: BIBLIOTECA COM A NOTE MÁXIMA, MENOR NOTA, MÉDIA E SITUAÇÃO

    By Davi M. Visintainer
    Dez - 2021
    """
    resultado = {'NOTA MÁXIMA': max(n), 'MENOR NOTA': min(n), 'MÉDIA DAS NOTAS': sum(n) / len(n)}
    if sit:
        if 0 <= resultado['MÉDIA DAS NOTAS'] < 5:
            resultado['SITUAÇÃO'] = 'PÉSSIMA'
        elif 5 <= resultado['MÉDIA DAS NOTAS'] < 7:
            resultado['SITUAÇÃO'] = 'RAZOÁVEL'
        elif resultado['MÉDIA DAS NOTAS'] >= 7:
            resultado['SITUAÇÃO'] = 'ÓTIMA'
    return resultado


# PROGRAMA PRINCIPAL
resposta = notas(5.5, 7.3, 6.1, sit=True)
help(notas)
print(resposta)
