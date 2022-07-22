"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""
n1 = float(input('Digite a primeira nota do aluno '))
n2 = float(input('Digite a segunda nota do alino: '))

média = (n1 + n2)/2

if média < 5.0:
    print('Sua média foi {:.1f}. Você está REPROVADO' .format(média))
elif 5.0 <= média < 7.0:
    print('A média do aluno foi {:.1f} e ele está de RECUPERAÇÃO' .format(média))
else:
    print('A média do aluno foi de {:.1f} e está APROVADO!' .format(média))
