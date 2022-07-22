"""
Crie um programa que declare uma matriz de dimensão 3×3
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = (int(input(f'Digite o valor da coordenada [{l + 1}, {c + 1}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^4}]', end='')
    print()