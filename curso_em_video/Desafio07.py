nome = input('Qual o nome do aluno?')

n1 = float(input('Digite a primeira nota do aluno {}: ' .format(nome)))
n2 = float(input('Digite a segunda nota do aluno {}: '.format(nome)))
m = (n1 + n2)/2

print('A média aritimética das notas do aluno {} é {}' .format(nome, m))

