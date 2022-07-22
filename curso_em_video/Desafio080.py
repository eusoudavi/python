"""
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
val = []
for c in range(1, 6):
    num = int(input(f'Digite o {c}º valor : '))
    if c == 1 or num > max(val):
        val.append(num)
    else:
        for pos in range(0, len(val)):
            if num <= val[pos]:
                val.insert(pos, num)
                break
print(val)
