"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
print('{:=^50}' .format(" Desafio 49 "))

n = int(input('Digite um número inteiro: '))
for x in range(1, 11):
    print("{} x {} = {}" .format(x, n, n * x))
