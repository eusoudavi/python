"""
Faça um programa que calcule a soma entre todos os
números IMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
print('{:=^50} \n' .format(' DESAFIO 48 '))
s = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s = s + n
        contador = contador + 1

# print(n)
print('A soma dos 500 primeiros números, que são múltiplos de 3 é {}. \n'
      'O total de números envolvidos nessa operação foram {}.' .format(s, contador))
