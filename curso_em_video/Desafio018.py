import math

a = float(input('Digite o valor de um ângulo: '))
# O valor lido pela funçaõ math.sin(a) é em radianos,
# então precisamos converter o valor escrito de graus para radianos
a = math.radians(a)

print('O valor do seno é {:.3f}'
      '\nO valor do cosseno é {:.3f}'
      '\nO valor da tangente é {:.3f}' .format(math.sin(a), math.cos(a), math.tan(a)))
