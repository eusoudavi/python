import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
print('-'*10)
print('O valor da hipotenusa é {:.2f}' .format(hip))

"""
# PODERIA SER RESOLVIDO APENAS NA MATEMÁRICA BÁSICA TAMBÉM
h = (co ** 2 + ca ** 2) ** (1 / 2)
print('O valor da hipotenusa calculada é {:.2f}' .format(h))
"""
print('-'*10)
a = math.acos(co/hip)
b = math.asin(co/hip)
print('O ângulo a é {:.3f}rad ou {:.2f}º'
      '\nO ângulo b é {:.3f}rad ou {:.2f}º' .format(a, math.degrees(a), b, math.degrees(b)))
