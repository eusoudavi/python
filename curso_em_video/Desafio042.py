"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
print('-*-' * 10)

if a == b == c:
    tipo = 'EQUILÁTERO'
elif a == b or b == c or a == c:
    tipo = 'ISÓCELES'
elif (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == b ** 2 + a ** 2):
    tipo = 'RETÂNGULO'
else:
    tipo = 'ESCALENO'

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    print('\033[30;42mAs retas {}, {} e {} podem formar um triangulo \033[m \n'
          '\033[34mEsse triângulo será {}\033[m'.format(a, b, c, tipo))
else:
    print('\033[30;41mAs retas {}, {} e {} NÃO podem formar um triangulo \033[m'.format(a, b, c))
print('-*-' * 10)
