# COMO EU FIZ
"""import math

n = float(input('Digite um valor real: '))
print('A parte inteira do valor {} é {:.1f}' .format(n, math.floor(n)))"""

# PODE UTILIZAR A FUNÇÃO TRUNCK
from math import trunc

n = float(input('Digite um valor real: '))
print('O valor inteiro do número {} é {}' .format(n, trunc(n)))
# PORÉM NÃO É NECESSÁRIO UTILIZAR A BIBLIOTECA MATH
print('O valor inteiro é {}' .format(int(n)))
