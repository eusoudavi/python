"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor inteiro na posição {c}: ')))
print(f'Os valores digitados foram: {valores}')
print('=*' * 30)
print(f'O maior valor digitado foi {max(valores)} na posição: ', end='')
for d in range(0, valores.count(max(valores))):
    if d == valores.count(max(valores)) - 1:
        print(f'{valores.index(max(valores), valores.index(max(valores)) + d)}')
    else:
        print(f'{valores.index(max(valores), valores.index(max(valores)) + d)}, ', end='')
print('=*' * 30)
print(f'O menor valor digitado foi {min(valores)} e está na posição: ', end='')
for d in range(0, valores.count(min(valores))):
    if d == valores.count(min(valores)) - 1:
        print(f'{valores.index(min(valores), valores.index(min(valores)) + d)}')
    else:
        print(f'{valores.index(min(valores), valores.index(min(valores)) + d)}, ', end='')
print('=*' * 30)
