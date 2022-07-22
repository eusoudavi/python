"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
final = [[], []]
for c in range(1, 8):
    leit = int(input(f'Digite o {c}º valor: '))
    if leit % 2 == 0:
        final[0].append(leit)
    else:
        final[1].append(leit)
final[0].sort()
final[1].sort()
print('=-' * 30)
print(f'A lista de valores pares é: {final[0]}')
print(f'A lista de valores impares é: {final[1]}')
