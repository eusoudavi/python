"""
Desenvolva um programa que leia
o comprimento de três retas e
diga ao usuário se elas podem
ou não formar um triângulo.
"""
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if abs(b - c) < a < b+c:
    # print('01')
    if abs(a - c) < b < a+c:
        # print('02')
        if abs(a - b) < c < a+b:
            print('As retas {}, {} e {} podem formar um triangulo' .format(a, b, c))
        else:
            print('As retas {}, {} e {} não podem formar um triangulo' .format(a, b, c))
    else:
        print('As retas {}, {} e {} não podem formar um triangulo'.format(a, b, c))
else:
    print('As retas {}, {} e {} não podem formar um triangulo'.format(a, b, c))
