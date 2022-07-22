import emoji
import math

# Apresentação inicial com um emoji
print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))

# Código rodando a biblioteca math
num = int(input('Digite um núemro inteiro:  '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é igual {:.4f}' .format(num, raiz))
print('A raiz quadrada arrendondada para cima de {} é igual {:.2f}' .format(num, math.ceil(raiz)))
print('A raiz quadrada arrendondada para baixo de {} é igual {:.2f}' .format(num, math.floor(raiz)))
