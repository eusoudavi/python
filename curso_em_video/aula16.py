"""
TUPLAS EM PYTHON
TUPLAS SÃO IMUTÁVEIS!!!
"""
# lache = (TUPLA) [LISTA] {DISCIONÁRIO}
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print((lanche[1]))
print(lanche[-1])
print(lanche[1:3])

print('=' * 40)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('=' * 40)
for cont in range(0, len(lanche)):
    print(cont)
print('=' * 40)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('=' * 40)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('=' * 40)

print(sorted(lanche))  # FAZ A ORDENAÇÃO DOS INTENS DA LISTA

a = (1, 2, 3)
b = (4, 5, 6, 7, 1)
c = a + b
print(c)
print(c.count(5))  # CONTA QUANTAS VEZES APARECE O ÍTEM 5
print(c.index(1))  # MOSTRA A POSIÇÃO DE 1 NA PRIMEIRA OCORRENCIA
print(c.index(1, 1))  # MOSTRA A POSIÇÃO DE 1 A PARTIR DA POSIÇÃO 1

del lanche  # APAGANDO A TUPLA lanche - NESSA VERSÃO DO PYTHON NÃO PRECISA UTILIZAR OS ()
