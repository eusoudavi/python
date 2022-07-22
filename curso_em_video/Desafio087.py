"""
Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
        B) A soma dos valores da terceira coluna.
            C) O maior valor da segunda linha.
"""
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = t3 = m2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = (int(input(f'Digite o valor da coordenada [{l + 1}, {c + 1}]: ')))
        if matrix[l][c] % 2 == 0:
            par += matrix[l][c]
        if l == 1 and matrix[l][c] > m2:
            m2 = matrix[l][c]
print('=-' * 30)
print(f' {"MATRIZ GERADA":^50} ')
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matrix[l][c]:^5} ]', end='')
    print()
print('=-' * 30)
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna são: {matrix[0][2] + matrix[1][2] + matrix[2][2]}')
print(f'O maior valor da segunda linha é {m2}')
print('=-' * 30)
