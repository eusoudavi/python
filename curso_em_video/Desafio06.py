n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)

print('O número que você digitou é o {}.'
      '\n O dobro desse número é {}'
      '\n O triplo desse número é {}'
      '\n A raiz quadrada desse número é {:.3f}' .format(n, d, t, rq))