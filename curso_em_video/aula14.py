"""
ESTRUTURA DE REPETIÇÃO - WHILE
"""
for a in range(1,10):
    print(a)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')). upper()
print('Fim')